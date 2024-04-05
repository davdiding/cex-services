import uvicorn

from app import app
from routers.binance_router import router as binance_router
from routers.okx_router import router as okx_router

app.include_router(okx_router, prefix="/okx", tags=["okx"])
app.include_router(binance_router, prefix="/binance", tags=["binance"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
