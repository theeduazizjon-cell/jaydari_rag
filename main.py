from contextlib import asynccontextmanager

from uvicorn.config import logger
from fastapi import FastAPI  # type: ignore
import uvicorn
import logging

from app.api.routes import router
from app.core.config import Settings

logger = logging.getLogger('uvicorn')
logger.info("**** JAYDARI RAG STARTS ****")


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = Settings()
    app.state.settings = settings
    yield

app = FastAPI(title='JAYDARI RAG', version='1.0.0', lifespan=lifespan)

app.include_router(router)
mn.k
