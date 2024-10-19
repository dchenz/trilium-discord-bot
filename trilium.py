import logging
from datautil import load_required_env
from trilium_py.client import ETAPI

logger = logging.getLogger(__name__)


class TriliumClient(ETAPI):
    def __init__(self):
        super().__init__(
            load_required_env("TRILIUM_URL"), load_required_env("TRILIUM_TOKEN")
        )

        appInfo = self.app_info()
        if appInfo.get("code") == "NOT_AUTHENTICATED":
            raise Exception("Token is invalid")
        logger.info(appInfo)


client = TriliumClient()
