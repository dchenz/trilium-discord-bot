import logging

import requests
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

    def get_note_content(self, noteId: str) -> str:
        # The library doesn't handle non-existent notes properly.
        url = f"{self.server_url}/etapi/notes/{noteId}/content"
        try:
            response = requests.get(url, headers=self.get_header())
            response.raise_for_status()
        except requests.exceptions.RequestException:
            raise Exception(response.content.decode("utf-8"))
        return response.content.decode("utf-8")


client = TriliumClient()
