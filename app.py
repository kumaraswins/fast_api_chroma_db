from fastapi import FastAPI
from router import operations
from router import file_operation, llm
app = FastAPI()


app.include_router(operations.router)
app.include_router(file_operation.router)
app.include_router(llm.router)

# Run the Application
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1",  port=8000)