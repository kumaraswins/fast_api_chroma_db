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
        collection = client.get_or_create_collection(name=old_name)
        collection.modify(name=new_name)
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


if __name__ == "__main__":
    print(create_collection("test"))
    #print(edit_collection())
    #print(create_collection("test"))
    print(edit_collection("test", "test1"))
    print(count_collection())


