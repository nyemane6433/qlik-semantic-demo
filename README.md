# 🔍 Qlik Semantic Search Demo

A demonstration project showcasing semantic search capabilities using MongoDB Atlas Vector Search, Voyage AI embeddings, and automated data pipelines. This repository enables you to generate synthetic application data, create vector embeddings, and perform intelligent semantic searches.

## 🎯 What This Demo Does

This project demonstrates:
- **Synthetic Data Generation**: Create realistic application names and descriptions at scale
- **Vector Embeddings**: Automatically generate embeddings using Voyage AI's `voyage-3-large` model
- **Semantic Search**: Perform intelligent searches that understand meaning, not just keywords
- **Real-time Updates**: Auto-update embeddings when documents change using Atlas Triggers

## ⚠️ Prerequisites

Before getting started, ensure you have:
- **Python 3.8+** installed on your system
- **MongoDB Atlas Account** with a cluster deployed
- **Voyage AI API Key** from [voyageai.com](https://voyageai.com)
- Basic familiarity with MongoDB and Python

## 📁 Project Structure

```text
qlik-semantic-demo/
├── data-pipeline/               # Python scripts for data orchestration
│   ├── sample.json              # Reference schema for documents
│   ├── generateNameDescriptions.py
│   ├── generateData.py
│   └── generateEmbeddings.py
├── indexes/                     # Indexes for search and vector search
│   ├── atlas-search-index.json  
│   └── atlas-vector-search-index.json
├── .env                         # API keys & DB strings (Keep this local!)
├── README.md                    # Project documentation
├── install.sh                   # Setup script for dependencies
├── requirements.txt             # Python package list
└── trigger.js                   # Atlas Function code for the trigger
```

## 🚀 Quick Start

### 1. 🐍 Set Up Python Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 2. ⚙️ Install Dependencies

```bash
pip3 install -r requirements.txt
```

Alternatively, use the provided install script:
```bash
./install.sh
```

### 3. 🔑 Configure Environment Variables

Create a `.env` file in the project root with the following variables:

```bash
# Voyage AI Configuration
VOYAGEAI_API_KEY=your_voyage_ai_api_key_here

# MongoDB Atlas Configuration
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/
MONGODB_DATABASE=qlik
MONGODB_COLLECTION=test
```

**Get your Voyage AI API Key**: Visit [voyageai.com](https://voyageai.com) and create an account to obtain your API key.

## 🎲 Data Generation Pipeline

### Step 1: Generate Names and Descriptions

Navigate to the data-pipeline folder and generate synthetic data:

```bash
cd data-pipeline
python3 generateNameDescriptions.py
```

This will create:
- **1,000,000** unique application descriptions
- **100,000** unique application names

### Step 2: Load Data into MongoDB

Edit `generateData.py` to configure your data load parameters:

```python
# Line 24
total_count = 10000  # Number of documents to generate

# Line 26
batch_size = 1000    # Documents per batch insert
```

Run the data loading script:

```bash
python3 generateData.py
```

### Step 3: 🧮 Generate Vector Embeddings

Once data loading is complete, generate embeddings for the `description` field using the Voyage AI `voyage-3-large` model (1024 dimensions):

```bash
python3 generateEmbeddings.py
```

This script will:
- Read all documents from your collection
- Generate embeddings for each description
- Store embeddings in the `description_embeddings` field

## 🔎 Atlas Search & Vector Search Setup

### Create Atlas Search Index

1. Navigate to your MongoDB Atlas cluster
2. Go to the **Search** tab
3. Click **Create Search Index**
4. Select **JSON Editor**
5. Copy the contents of `indexes/atlas-search-index.json`
6. Paste into the editor and create the index

### Create Atlas Vector Search Index

1. In the **Search** tab, click **Create Search Index**
2. Select **Atlas Vector Search**
3. Choose **JSON Editor**
4. Copy the contents of `indexes/atlas-vector-search-index.json`
5. Paste into the editor and create the index

## ⚡ Create Atlas Trigger for Auto-Updates

Set up an Atlas Trigger to automatically update embeddings when documents are modified.

### Trigger Configuration

1. Navigate to **Triggers** in your Atlas cluster
2. Click **Add Trigger**
3. Configure with the following settings:

**Trigger Details:**
- **Trigger Type**: Database
- **Watch Against**: Collection
- **Cluster Name**: qlik
- **Database Name**: qlik
- **Collection Name**: test
- **Operation Type**: Select all three:
  - ✅ Insert Document
  - ✅ Update Document
  - ✅ Replace Document
- **Full Document**: Toggle **ON**
- **Document Pre-image**: Leave **OFF**

**Event Type:**
- **Select An Event Type**: Function
- **Function**: Select **+New Function** from dropdown
- **Function Name**: `updateEmbeddings`
- **Function Code**: Copy and paste the code from `trigger.js`
- **Trigger Name**: `updateEmbeddings`

4. Click **Save** to activate the trigger

## 📊 Configuration Details

### Embedding Model
- **Model**: `voyage-3-large`
- **Dimensions**: 1024
- **Use Case**: Optimized for semantic search and retrieval tasks

## 🔗 Useful Links

- [MongoDB Atlas Documentation](https://www.mongodb.com/docs/atlas/)
- [MongoDB Atlas Search](https://www.mongodb.com/docs/atlas/atlas-search/)
- [MongoDB Atlas Vector Search](https://www.mongodb.com/docs/atlas/atlas-vector-search/vector-search-overview/)
- [Voyage AI Documentation](https://docs.voyageai.com/)
- [Atlas Triggers Documentation](https://www.mongodb.com/docs/atlas/app-services/triggers/)

---

