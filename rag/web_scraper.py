"""
querying the url 
"""
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from config import embedings


def main(url, query):
    loader = WebBaseLoader(url)
    docs = loader.load()
    documents = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50).split_documents(docs)
    vectordb = Chroma.from_documents(
        documents=documents,
        embedding=embedings.embeddings,
        collection_name=embedings.ollama_collection,
    )
    retriever = vectordb.as_retriever(search_kwargs={"k": embedings.target_source_chunks})
    result = retriever.get_relevant_documents(query)
    docs = retriever.invoke(query)
    print(docs)
    print("")
    print(result)
    json = {"page_content" : result[0].page_content}
    return json

if __name__ == "__main__":
    url = "https://finshots.in/archive/america-sues-apple/?utm_medium=Whatsapp&utm_source=Finshots_App_User"
    query = "green bubble "
    print((main(url, query)))
    