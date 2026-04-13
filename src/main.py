from contextlib import asynccontextmanager

import logging
import uvicorn
import sys
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

sys.path.append(str(Path(__file__).parent.parent))

from src.app.presentation.api.auth import router as router_auth

logging.basicConfig(level=logging.INFO)

app = FastAPI()
app.include_router(router_auth)


app.add_middleware(CORSMiddleware, allow_origins=["*"])


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)