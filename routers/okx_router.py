from fastapi import APIRouter, Query

from app import app
from utils import response_helper

router = APIRouter()


@router.get("/sync-exchange-info")
async def sync_exchange_info():
    try:
        res = await app.state.okx_public.sync_exchange_info()
        return response_helper(0, "successfully sync exchange info", res)
    except Exception as e:
        return response_helper(1, str(e))


@router.get("/get-exchange-info")
async def get_exchange_info(market_type: str = None):
    try:
        res = await app.state.okx_public.get_exchange_info(market_type=market_type)
        return response_helper(0, "successfully get exchange info", res)
    except Exception as e:
        return response_helper(1, str(e))


@router.get("/get-tickers")
async def get_tickers(market_type: str = None):
    try:
        res = await app.state.okx_public.get_tickers(market_type=market_type)
        return response_helper(0, "successfully get tickers", res)
    except Exception as e:
        return response_helper(1, str(e))


@router.get("/get-ticker")
async def get_ticker(instrument_id: str = Query(..., description="instrument id")):
    try:
        res = await app.state.okx_public.get_ticker(instrument_id=instrument_id)
        return response_helper(0, "successfully get ticker", res)
    except Exception as e:
        return response_helper(1, str(e))


@router.get("/get-klines")
async def get_klines(
    instrument_id: str = Query(...), interval: str = Query(...), start: int = None, end: int = None, num: int = 30
):
    try:
        res = await app.state.okx_public.get_klines(instrument_id, interval, start=start, end=end, num=num)
        return response_helper(0, "successfully get klines", res)
    except Exception as e:
        return response_helper(1, str(e))


@router.get("/get-current-funding-rate")
async def get_current_funding_rate(instrument_id: str = Query(...)):
    try:
        res = await app.state.okx_public.get_current_funding_rate(instrument_id=instrument_id)
        return response_helper(0, "successfully get current funding rate", res)
    except Exception as e:
        return response_helper(1, str(e))


@router.get("/get-history-funding-rate")
async def get_history_funding_rate(instrument_id: str = Query(...), start: int = None, end: int = None, num: int = 30):
    try:
        res = await app.state.okx_public.get_history_funding_rate(
            instrument_id=instrument_id, start=start, end=end, num=num
        )
        return response_helper(0, "successfully get history funding rate", res)
    except Exception as e:
        return response_helper(1, str(e))


# Private endpoint


@router.get("/get-account-info")
async def get_account_info():
    try:
        res = await app.state.okx_private.get_account_info()
        return response_helper(0, "successfully get account info", res)
    except Exception as e:
        return response_helper(1, str(e))


@router.get("/get-balance")
async def get_balance():
    try:
        res = await app.state.okx_private.get_balance()
        return response_helper(0, "successfully get balance", res)
    except Exception as e:
        return response_helper(1, str(e))


@router.get("/get-positions")
async def get_positions():
    try:
        res = await app.state.okx_private.get_positions()
        return response_helper(0, "successfully get positions", res)
    except Exception as e:
        return response_helper(1, str(e))


@router.get("/place-market-order")
async def place_market_order(instrument_id: str, side: str, volume: float, in_quote: bool = False):
    try:
        res = await app.state.okx_private.place_market_order(
            instrument_id=instrument_id, side=side, volume=volume, in_quote=in_quote
        )
        return response_helper(0, "successfully place market order", res)
    except Exception as e:
        return response_helper(1, str(e))


@router.get("/place-limit-order")
async def place_limit_order(instrument_id: str, side: str, price: float, volume: float, in_quote: bool = False):
    try:
        res = await app.state.okx_private.place_limit_order(
            instrument_id=instrument_id, side=side, price=price, volume=volume, in_quote=in_quote
        )
        return response_helper(0, "successfully place limit order", res)
    except Exception as e:
        return response_helper(1, str(e))


@router.get("/cancel-order")
async def cancel_order(instrument_id: str, order_id: int):
    try:
        res = await app.state.okx_private.cancel_order(instrument_id=instrument_id, order_id=order_id)
        return response_helper(0, "successfully cancel order", res)
    except Exception as e:
        return response_helper(1, str(e))


@router.get("/get-opened-orders")
async def get_opened_orders(market_type: str = None, instrument_id: str = None):
    try:
        res = await app.state.okx_private.get_opened_orders(instrument_id=instrument_id, market_type=market_type)
        return response_helper(0, "successfully get opened orders", res)
    except Exception as e:
        return response_helper(1, str(e))
