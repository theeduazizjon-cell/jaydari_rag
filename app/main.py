from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn
import logging

from app.api.routes import router
from app.core.config import settings

logger = logging.getLogger('uvicorn')
logger.info("**** JAYDARI RAG STARTS ****")


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.settings = settings
    yield

app = FastAPI(title='JAYDARI RAG', version='1.0.0', lifespan=lifespan)

app.include_router(router)


if __name__ == '__main__':
    uvicorn.run('app.main:app', reload=True)
