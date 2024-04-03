import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.embeddings import OllamaEmbeddings

target_source_chunks = 2
ollama_collection = "ollama_embeds"
embeddings_model_name = os.environ.get('EMBEDDINGS_MODEL_NAME',"all-MiniLM-L6-v2")
embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)


