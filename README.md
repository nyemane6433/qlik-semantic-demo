# Qlik Semantic Search Demo
Repository for demo files to generate data and indexes for semantic search demo at Qlik

### Files
```requirements.txt``` python packages to install

```sample.json`` sample schema 


```.env``` sets MONGODB_URL, DATABASE, COLLECTION, and VOYAGEAI_API_KEY as environment variables. Please create and set your own ```VOYAGEAI_API_KEY``` from voyageai.com


```.generateNameDescription.py``` generates a list of app namess and descriptions. The execution of the ```generateNameDescriptions.py``` will generate app.txt. and description.txt. 


```.generateData.py``` generates batches of record to insert into MongoDB Cluster


```.generateEmbeddings.py``` generates embeddings for description and store embeddings in ```description_embeddings``` field


```atlas-search-index.json``` is the Atlas Search Index Mapping


```atlas-vector-search-index.json``` is the Atlas Vector Search Index Mapping


```trigger.json``` Atlas Trigger function to update ```description_embeddings``` when document is updated

## Data Generation


.
