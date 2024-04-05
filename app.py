from contextlib import asynccontextmanager

from cex_adaptors.okx import Okx
from fastapi import FastAPI

from utils import get_auth_data


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.okx_public = Okx()
    app.state.okx_private = Okx(**get_auth_data(exchange="okx", name="OKX_DEFAULT_DEMO_1"))
    await app.state.okx_public.sync_exchange_info()
    await app.state.okx_private.sync_exchange_info()
    yield

    await app.state.okx_public.close()
    await app.state.okx_private.close()


app = FastAPI(lifespan=lifespan)
