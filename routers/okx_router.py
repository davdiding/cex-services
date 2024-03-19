from cex_adaptors.okx import Okx
from fastapi import APIRouter

from app import app
from utils import response_helper

router = APIRouter()

app.state.okx_instance: Okx


@router.get("/sync_exchange_info")
async def sync_exchange_info():
    try:
        res = await app.state.okx_instance.sync_exchange_info()
        return response_helper(0, "successfully sync exchange info", res)
    except Exception as e:
        return response_helper(1, str(e))


@router.get("/get_exchange_info")
async def get_exchange_info(market_type: str = None):
    try:
        res = await app.state.okx_instance.get_exchange_info(market_type=market_type)
        return response_helper(0, "successfully get exchange info", res)
    except Exception as e:
        return response_helper(1, str(e))


@router.get("/get_tickers")
async def get_tickers(market_type: str = None):
    try:
        res = await app.state.okx_instance.get_tickers(market_type=market_type)
        return response_helper(0, "successfully get tickers", res)
    except Exception as e:
        return response_helper(1, str(e))
