import logging
import os

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
