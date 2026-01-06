# Qlik Semantic Search Demo
This repository contains the utilities and configuration files required to generate synthetic application data, index it in MongoDB Atlas, and perform semantic search using Voyage AI embeddings.

### Files

```text
qlik-semantic-demo/
├── data-pipeline/               # Python scripts for data orchestration
│   ├── sample.json              # Reference schema for documents
│   ├── generateNameDescriptions.py
│   ├── generateData.py
│   └── generateEmbeddings.py
├── indexes/                     # indexes for search and vector search
│   ├── atlas-search-index.json  
│   └── atlas-vector-search-index.json
├── .env                         # API keys & DB strings (Keep this local!)
├── README.md                    # Project documentation
├── install.sh                   # Setup script for dependencies
├── requirements.txt             # Python package list
└── trigger.js                   # Atlas Function code for the trigger
```
## Install Dependencies
```pip3 install -r requirements.txt```

## Configure ```.env``` Variables
Deploy a VOYAGEAI_API_KEY from https://voyageai.com and set to VOYAGEAI_API_KEY

## Data Generation
Navigate to data-pipeline folder: ```cd data-pipeline```

### Generate Name and Description
Generate 1M different descriptions and 100K application names.

Run ```python3 generateNameDescriptions.py```

### Load Data
In ```.generateData.py``` modify ```total_count``` (line 24) and ```batch_size``` (line 26).

```total_count``` is the number of json records to load.

```batch_size``` is the number of json records in each batch of insert_many.

Run ```python3 generateData.py```

## Generate Embeddings
Once the data load is complete, run ```generateEmbeddings``` to set ```description_embeddings``` field. We are currently using ```voyage-3-large``` model with 1024 dimensions. 

Run ```python3 generateEmbeddings.py```

## Atlas Search & Vector Search
Create an Atlas Search Index in the UI using the index mapping in ```atlas-search-index.json```. Create an Atlas Vector Search Index in the UI using the index mapping in ```atlas-vector-search-index.json```.

## Create Atlas Trigger
Atlas Triggers and Functions to update the description_embeddings when document is inserted, updated, and replaced. 

### Trigger Details
<mark>**Trigger Type**</mark>: **Database**

<mark>**Watch Against**</mark>: **Collection**

<mark>**Cluster Name**</mark>: **qlik**

<mark>**Database Name**</mark>: **qlik**

<mark>**Collection Name**</mark>: **test**

<mark>**Operation Type**</mark>: ```Insert Document``` ```Update Document``` ```Replace Document```

<mark>**Full Document**</mark>: **Toggle ON**

<mark>**Document Pre-image**</mark>: **Do not enable**

### Event Type

<mark>**Select An Event Type**</mark>: **function**

<mark>**Function**</mark>: **Select ```+New Function``` from drop down**

<mark>**Function Name**</mark>: **updateEmbeddings**

<mark>**Function**</mark>: **copy and paste the function in ```trigger.js```**

<mark>**Trigger Name**</mark>: **updateEmbeddings**







.
