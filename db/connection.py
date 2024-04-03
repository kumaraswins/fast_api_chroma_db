import chromadb
client = chromadb.Client()


def create_collection(name:str) -> str:
    try:
        collection = client.create_collection(name)
        return collection
    except Exception as e:
        return f"Error occured , `{e}`"
        

def list_all_collection() -> list:
    return client.list_collections()


def edit_collection(old_name:str, new_name:str) -> str:
    try:
        #collection = client.get_or_create_collection(name=old_name)
        collection = client.get_collection(name=old_name)
        collection.modify(name=new_name)
        return collection
    except Exception as e:
        return f"Error occured , {e}"


def get_client_ref(name:str) -> object:
    try:
        #collection = client.get_or_create_collection(name=old_name)
        collection = client.get_collection(name=name)
        return collection
    except Exception as e:
        return f"Error occured , {e}"


def count_collection() -> str:
    try:
        return len(client.list_collections())
    except Exception as e:
        return f"Error occured , {e}"


def delete_collection(name:str) -> str:
    try:
        collection = client.delete_collection(name=name)
        return f"Deleted the collection {name}"
    except Exception as e:
        return f"Error occured , {e}"

def add_docs_to_collection(name:str, document:object):
    collection = client.get_or_create_collection(name=name)
    collection.add(
    documents=["lorem ipsum...", "doc2", "doc3", ...],
    metadatas=[{"chapter": "3", "verse": "16"}, {"chapter": "3", "verse": "5"}, {"chapter": "29", "verse": "11"}, ...],
    ids=["id1", "id2", "id3", ...]
)

if __name__ == "__main__":
    print(create_collection("test"))
    #print(edit_collection())
    #print(create_collection("test"))
    print(edit_collection("test", "test1"))
    print(count_collection())


