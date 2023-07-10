
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app.api.endpoints.routes import router as delivery_router

import uvicorn
import os

port = int(os.environ.get("PORT", 8000))
print(port)

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
    # parser = argparse.ArgumentParser(description='FIX Client')
    # parser.add_argument('-c', '--configfile', default="clientLocal.cfg", help='file to read the config from')
    # args = parser.parse_args()
    # main(args.configfile)
    uvicorn.run(
        "api.main:app",
        host="127.0.0.1",
        port=port,
        ssl_keyfile="private.key",
        ssl_certfile="certificate.crt",
        reload=True,
    )
