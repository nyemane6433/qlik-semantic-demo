import json
import os
import pymongo
import voyageai
from pymongo import MongoClient, UpdateOne
from dotenv import load_dotenv


load_dotenv()
# mongodb
uri = os.environ["MONGO_URL"]
client = pymongo.MongoClient(uri)
database = client[os.environ["DATABASE"]]
collection = database[os.environ["COLLECTION"]]


### Generate embeddings for data inserted (existing) in mongodb - bulk write embeddings
def generate_embeddings():

    api = voyageai.Client(api_key="") # deploy a voyage ai api key
    results = collection.find({'description_embeddings': {'$exists': False}})

    api_batch_size = 100
    batch = []
    count = 0
    total_updated = 0


    for doc in results:

        batch.append(doc)

        if len(batch) == api_batch_size:
            # 100 descriptions per voyage api request
            descriptions = [d['description'] for d in batch]
            desc_embedding = api.embed(descriptions, model="voyage-3-large", input_type="document")

            # bulk write
            updates = []
            for i, embedding in enumerate(desc_embedding.embeddings):
                updates.append(UpdateOne(
                    {'_id': batch[i]['_id']}, 
                    {'$set': {'description_embeddings': embedding}}
                ))

            collection.bulk_write(updates)
            total_updated += len(updates)
            print(f"Progress: {total_updated} documents updated...")

            # reset batch size
            batch = []
    
    if batch:
        collection.bulk_write(updates)
        print(f"Update complete. Total: {count + len(updates)}")

if __name__ == "__main__":
    generate_embeddings()