import logging
import os

import requests

from trilium_client import trilium_client
from utils import loadRequiredEnv

logger = logging.getLogger(__name__)


def createClient() -> trilium_client.DefaultApi:
    apiClient = trilium_client.ApiClient(
        configuration=trilium_client.Configuration(
            host=loadRequiredEnv("TRILIUM_URL"),
        ),
    )
    client = trilium_client.DefaultApi(apiClient)
    token = None

    password = os.getenv("TRILIUM_PASSWORD")
    if password:
        response = client.login(trilium_client.LoginRequest(password=password))
        token = response.auth_token

    if not token:
        token = loadRequiredEnv("TRILIUM_TOKEN")

    apiClient.default_headers["Authorization"] = token
    return client


client = createClient()

logger.info(client.get_app_info())


def setAttachmentContents(attachmentId: str, data: bytes):
    """
    Updates the contents of an existing attachment identified by its `attachmentId` with the
    provided binary data.

    This function is preferred over `trilium.client.put_attachment_content_by_id` because it
    correctly serializes the request body, preventing attachment corruption.
    """
    response = requests.put(
        f"{client.api_client.configuration.host}/attachments/{attachmentId}/content",
        data=data,
        headers={
            "Authorization": client.api_client.default_headers.get("Authorization"),
            "Content-Type": "application/octet-stream",
        },
    )
    response.raise_for_status()
