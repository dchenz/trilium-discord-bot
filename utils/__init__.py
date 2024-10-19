import os
import sys
from typing import Any

import tabulate


def loadRequiredEnv(name: str) -> str:
    """
    Reads an environment variable, and if the value is empty, the program terminates with status
    code 1.
    """
    value = os.getenv(name)
    if not value:
        sys.exit(f"Missing {name} environment variable")
    return value


def formatAsTable(records: list[dict[str, Any]], fieldsToPick: list[str]) -> str:
    """
    Formats a list of dictionaries into a table, assuming all dictionaries have the same keys.
    """
    headers = {field: field for field in fieldsToPick}
    formatted = tabulate.tabulate(records, headers=headers)
    return f"```\n{formatted}\n```"


def pickDictKeys(record: dict[str, Any], fields: list[str]) -> dict[str, Any]:
    """
    Returns a new dictionary containing only a selected set of keys.
    """
    return {k: record[k] for k in record if k in fields}
