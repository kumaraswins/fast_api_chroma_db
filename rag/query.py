"""
querying the knowledge base
"""

import os
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.vectorstores import Chroma
from langchain.llms import Ollama

embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME","all-MiniLM-L6-v2")
persist_directory = os.environ.get('PERSIST_DIRECTORY','storage')
model_type = os.environ.get('MODEL_TYPE',"mistral")
source_directory = os.environ.get('SOURCE_DIRECTORY', 'source_documents')
embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)
target_source_chunks = int(os.environ.get('TARGET_SOURCE_CHUNKS',4))
llm = Ollama(model=model_type, callbacks=[StreamingStdOutCallbackHandler()])


def main(data):
    knowledge = f"{persist_directory}/{data.collection_name}"
    if(os.path.isdir(knowledge)):
        db = Chroma(persist_directory=knowledge, embedding_function=embeddings)
        retriever = db.as_retriever(search_kwargs={"k": target_source_chunks})
        qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True)
        res = qa(data.query)
        answer, docs = res['result'], res['source_documents']
        return {"results": answer, "docs":docs}
    else:
        return {"results": "No collections found", "docs":[]}
    

def nlp(data):
    knowledge = f"{persist_directory}/{data.collection_name}"
    if(os.path.isdir(knowledge)):
        db = Chroma(persist_directory=knowledge, embedding_function=embeddings)
        retriever = db.as_retriever(search_kwargs={"k": target_source_chunks})
        qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True)
        res = qa(data.query)
        answer, docs = res['result'], res['source_documents']
        return {"results": answer, "docs":docs}
    else:
        return {"results": "No collections found", "docs":[]}