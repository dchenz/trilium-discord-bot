import logging

from trilium_py.client import ETAPI

from datautil import loadRequiredEnv

logger = logging.getLogger(__name__)


class TriliumClient(ETAPI):
    def __init__(self):
        super().__init__(loadRequiredEnv("TRILIUM_URL"), loadRequiredEnv("TRILIUM_TOKEN"))

        appInfo = self.app_info()
        if appInfo.get("code") == "NOT_AUTHENTICATED":
            raise Exception("Token is invalid")
        logger.info(appInfo)


client = TriliumClient()
