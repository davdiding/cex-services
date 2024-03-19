from contextlib import asynccontextmanager

from cex_adaptors.okx import Okx
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.okx_instance = Okx()
    await app.state.okx_instance.sync_exchange_info()
    yield

    await app.state.okx_instance.close()


app = FastAPI(lifespan=lifespan)
