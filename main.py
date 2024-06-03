from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
from datetime import datetime
from guestbook import guestbook_router
import uvicorn

app = FastAPI()

origins = [
    "http://35.173.37.0",
    "http://35.173.37.0:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


    

app.include_router(guestbook_router)
if __name__ == '__main__':
    uvicorn.run("main:app", host = "0.0.0.0", port=8000, reload=True)



