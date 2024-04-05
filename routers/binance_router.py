from cex_adaptors.binance import Binance
from fastapi import APIRouter, Query

from app import app
from utils import response_helper

router = APIRouter()
app.state.binance_public: Binance


@router.get("/sync-exchange-info")
async def sync_exchange_info():
    try:
        res = await app.state.binance_public.sync_exchange_info()
        return response_helper(0, "successfully sync exchange info", res)
    except Exception as e:
        return response_helper(1, str(e))


@router.get("/get-exchange-info")
async def get_exchange_info(market_type: str = None):
    try:
        res = await app.state.binance_public.get_exchange_info(market_type=market_type)
        return response_helper(0, "successfully get exchange info", res)
    except Exception as e:
        return response_helper(1, str(e))


@router.get("/get-tickers")
async def get_tickers(market_type: str = None):
    try:
        res = await app.state.binance_public.get_tickers(market_type=market_type)
        return response_helper(0, "successfully get tickers", res)
    except Exception as e:
        return response_helper(1, str(e))


@router.get("/get-ticker")
async def get_ticker(instrument_id: str = Query(..., description="instrument id")):
    try:
        res = await app.state.binance_public.get_ticker(instrument_id=instrument_id)
        return response_helper(0, "successfully get ticker", res)
    except Exception as e:
        return response_helper(1, str(e))


@router.get("/get-klines")
async def get_klines(
    instrument_id: str = Query(...), interval: str = Query(...), start: int = None, end: int = None, num: int = 30
):
    try:
        res = await app.state.binance_public.get_klines(instrument_id, interval, start=start, end=end, num=num)
        return response_helper(0, "successfully get klines", res)
    except Exception as e:
        return response_helper(1, str(e))


@router.get("/get-history-funding-rate")
async def get_history_funding_rate(instrument_id: str = Query(...), start: int = None, end: int = None, num: int = 30):
    try:
        res = await app.state.binance_public.get_history_funding_rate(
            instrument_id=instrument_id, start=start, end=end, num=num
        )
        return response_helper(0, "successfully get history funding rate", res)
    except Exception as e:
        return response_helper(1, str(e))
