import json
import os
import uuid
import random
import pymongo
from datetime import datetime, timedelta
from faker import Faker
from bson import ObjectId
from dotenv import load_dotenv


load_dotenv()
# mongodb
uri = os.environ["MONGO_URL"]
client = pymongo.MongoClient(uri)
database = client[os.environ["DATABASE"]]
collection = database[os.environ["COLLECTION"]]

# Initialize Faker
fake = Faker()

def generate_metadata():

    total_count = 100 # total count of records to generate
    batch = []
    batch_size = 2 # batch size for inserts
    inserted = 0

    for i in range(1, total_count+1):
    # load app names and description 
        with open("app.txt", "r", encoding="utf-8") as f:
        # .strip() removes the newline character (\n) from each line
            app_array = [line.strip() for line in f]
            name = random.choice(app_array)

        with open("desc.txt", "r", encoding="utf-8") as f:
        # .strip() removes the newline character (\n) from each line
            desc_array = [line.strip() for line in f]
            desc = random.choice(desc_array)
        
        type = ['SHARED', 'DATA', 'MANAGED', 'PERSONAL']
        space = [
            {
                "id": str(uuid.uuid4()),
                "name": "sales-dev-analytics"
            },
            {
                "id": str(uuid.uuid4()),
                "name": "finance-test-analytics"
            },
            {
                "id": str(uuid.uuid4()),
                "name": "sales-uat-analytics"
            },
            {
                "id": str(uuid.uuid4()),
                "name": "finance-uat-analytics"
            },
            {
                "id": str(uuid.uuid4()),
                "name": "sales-prod-analytics"
            },

        ]

        usage = ['ANALYTICS', 'MONITRING', 'ODAG', 'LINK', 'DATA_PREP', 'REPORTING']
        tenant_id =fake.bothify(text='??#??#??-???_??#??##?##?#')
        relationship_id = str(uuid.uuid4()) 
        owner_id = fake.hexify(text='^^^^^^^^^^^^^^^^^^^^^^^^')
        data = {
            "relationshipId": relationship_id,
            "id": "",
            "tenantId": tenant_id,
            "type": random.choice(type)
        }
        json_str = json.dumps(data, separators=(',', ':'))
        uniqueResource_id = json_str.encode('utf-8').hex()
        created_at = fake.date_time_between(start_date='-2y', end_date='now')
        updated_at = created_at + timedelta(days=7)
        extensions = ['qvf', 'qvd', 'json', 'png', 'xls', 'pdf']
        selected_ext = random.choice(extensions)
        filename = fake.file_name(extension=selected_ext)


        payload = {
            "name": name,
            "description": desc,
            "thumbnailId": f"/api/v1/apps/{str(uuid.uuid4())}/media/files/{filename}",
            "tenantId": tenant_id,
            "createdAt": created_at,
            "updatedAt": updated_at,
            "collectionMemberships": [
                {
                    "id": ObjectId(),
                    "addedAt": updated_at,
                    "addedBySubject": f"DOMAIN\\{fake.last_name().upper()}"
                }
            ],
            "resourceType": "app",
            "resourceSubType": "test",
            "resourceId": str(uuid.uuid4()),
            "resourceAttributes": [
                {"usage": random.choice(usage)},
                {"description": desc},
                {"id": str(uuid.uuid4())},
                {"name": name},
                {"_resourcetype": "app"},
                {"createdDate": created_at},
                {"thumbnail": f"/api/v1/apps/e04b2c9f-2bc0-44d8-9f52-313db1403048/media/files/{filename}"},
                {"published": False},
                {"isDirectQueryMode": False},
                {"hasSectionAccess": False},
                {"owner": "Qlik\\{owner_id}"},
                {"ownerId": owner_id},
                {"modifiedDate": updated_at},
                {"lastReloadTime": updated_at}
            ],
            "resourceCreatedAt": created_at,
            "resourceUpdatedAt": updated_at,
            "creatorId": owner_id,
            "ownerId": owner_id,
            "space": random.choice(space),
            "parents": {
                "uniqueResourceId": uniqueResource_id
            },
            "resourceSize": {
                "appFile": random.randint(100000, 500000),
                "appMemory": random.randint(50000, 300000)
            }
        }

        batch.append(payload)

        if len(batch) == batch_size:
            collection.insert_many(batch)
            inserted += len(batch)
            print(f"Inserted: {inserted} / {total_count}")
            batch = []  # Clear the batch list to free up RAM

    # insert remaining docs
    if batch:
        collection.insert_many(batch)
        print(f"Final insertion complete. Total: {total_count}")


if __name__ == "__main__":
    generate_metadata()