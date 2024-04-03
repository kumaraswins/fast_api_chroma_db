# import
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
from langchain_text_splitters import CharacterTextSplitter
import uuid

#from langchain_community.embeddings import HuggingFaceEmbeddings
SOURCE_DOCUMENTS  = "source_documents"

# load the document and split it into chunks
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
#embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def get_raw_text_doc(file_name:str) -> object:
    loader = TextLoader(f"{SOURCE_DOCUMENTS}/{file_name}")
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    docs =  text_splitter.split_documents(documents)
    json = {"docs":[],"meta":[],"id":[]}
    for index ,s in enumerate(docs):
        json['docs'].append(s.page_content)
        json['meta'].append(s.metadata)
        json['id'].append(str(uuid.uuid1()))
    return json

# for s in docs:
#     print(f"{len(s.page_content)}\n")
#     print(f"{s.metadata}\n")

#create the open-source embedding function
    
# # load it into Chroma
# db = Chroma.from_documents(docs, embeddings)
# print(db)

# # query it
# query = "What did the president say about Ketanji Brown Jackson"
# docs = db.similarity_search(query)

# # print results
# print(docs[0].page_content)