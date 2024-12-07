from dotenv import load_dotenv
import os

from pymongo import MongoClient
from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain_community.vectorstores import MongoDBAtlasVectorSearch
from langchain_community.document_loaders import DirectoryLoader

load_dotenv()

# Init directory loader
loader = DirectoryLoader('./sample_files', glob="./*.txt", show_progress=True)
data = loader.load()

# Setup MongoDB connection
mongo_uri = os.getenv('MONGO_URI')
client = MongoClient(mongo_uri)
collection = client["langchain_demo"]["collection_of_text_blobs"]

# Define OpenAI embeddings model
embeddings = OpenAIEmbeddings()

# Initialize VectorStore
vectorStore = MongoDBAtlasVectorSearch.from_documents(data, embeddings, collection=collection)

print(vectorStore)