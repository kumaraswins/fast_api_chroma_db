import os
from dotenv import load_dotenv
from chromadb.config import Settings

load_dotenv()

# Define the folder for storing database
PERSIST_DIRECTORY = os.environ.get('PERSIST_DIRECTORY', "storage")
EMBEDDINGS_MODEL_NAME = "all-MiniLM-L6-v2"
model_type = "mistral"
source_directory =  'source_documents'


# Define the Chroma settings
CHROMA_SETTINGS = Settings(
        persist_directory=PERSIST_DIRECTORY,
        anonymized_telemetry=False
)