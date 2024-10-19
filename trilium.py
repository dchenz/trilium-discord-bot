import logging

from trilium_py.client import ETAPI

logger = logging.getLogger(__name__)

client: ETAPI = None  # type: ignore


def login(url: str, token: str) -> ETAPI:
    global client
    if client:
        client.close()
    client = ETAPI(url, token)
    logger.info(client.app_info())
    return client
