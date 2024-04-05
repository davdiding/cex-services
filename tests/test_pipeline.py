from unittest import IsolatedAsyncioTestCase

import requests as rq

base_url = "http://127.0.0.1:8000"


class TestOkxService(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.prefix = "/okx"

    async def test_get_exchange_info(self):
        url = base_url + self.prefix + "/get-exchange-info"
        response = rq.get(url).json()
        self.assertTrue(response["code"] == 0)
        return

    async def test_get_tickers(self):
        url = base_url + self.prefix + "/get-tickers"
        response = rq.get(url).json()
        self.assertTrue(response["code"] == 0)
        return


class TestBinance(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.prefix = "/binance"

    async def test_get_exchange_info(self):
        url = base_url + self.prefix + "/get-exchange-info"
        response = rq.get(url).json()
        self.assertTrue(response["code"] == 0)
        return

    async def test_get_tickers(self):
        url = base_url + self.prefix + "/get-tickers"
        response = rq.get(url).json()
        self.assertTrue(response["code"] == 0)
        return
