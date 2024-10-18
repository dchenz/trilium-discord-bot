from trilium_py.client import ETAPI

client: ETAPI = None  # type: ignore


def login(url: str, token: str) -> ETAPI:
    global client
    if client:
        client.close()
    client = ETAPI(url, token)
    return client
