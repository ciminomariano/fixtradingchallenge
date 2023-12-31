import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app.api.endpoints.routes import router as delivery_router

import uvicorn
import os


port = int(os.environ.get("PORT", 8000))

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(delivery_router)

if __name__ == "__main__":

    uvicorn.run(
        "app.api.main:app",
        host="0.0.0.0",
        port=port,
        ssl_keyfile="private.key",
        ssl_certfile="certificate.crt",
        reload=True,
    )
