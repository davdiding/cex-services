from cex_adaptors.okx import Okx

okx_instance = None


async def get_okx_instance():
    global okx_instance
    okx_instance = Okx()
    await okx_instance.sync_exchange_info()
    return okx_instance
