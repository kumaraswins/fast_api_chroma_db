from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from router import operations
app = FastAPI()


app.include_router(operations.router)


# Run the Application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)