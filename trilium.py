import logging

from trilium_py.client import ETAPI

logger = logging.getLogger(__name__)

client: ETAPI = None  # type: ignore


def login(url: str, token: str) -> ETAPI:
    global client
    if client:
        client.close()
    client = ETAPI(url, token)

    appInfo = client.app_info()
    if appInfo.get("code") == "NOT_AUTHENTICATED":
        raise Exception("Token is invalid")
    logger.info(appInfo)

    return client
