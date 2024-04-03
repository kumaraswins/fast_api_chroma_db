import ollama
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
#SYSTEM = "You are a financial assistant, you help to classify the expenses and income from the bank transactions"
SYSTEM = "You are an indian historian knowing facts  {topic}"
WORD_LIMIT = ",let it be short answer"

model = Ollama(model="mistral")
def main(query):
    prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                SYSTEM + WORD_LIMIT,
            ),
            ("human", "input")]
    )
    chain = prompt | model
    #{"topic": "ice cream"}
    #response = chain.invoke({"input": query})
    response = chain.invoke({"topic": "who was Ashoka"})
    return(response)

if __name__ == "__main__":
    print(main("who are you"))