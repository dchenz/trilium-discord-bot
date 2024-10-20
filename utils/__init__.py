import os
import sys


def loadRequiredEnv(name: str) -> str:
    """
    Reads an environment variable, and if the value is empty, the program terminates with status
    code 1.
    """
    value = os.getenv(name)
    if not value:
        sys.exit(f"Missing {name} environment variable")
    return value


def partitionList(xs: list, n: int) -> list:
    return [xs[i : i + n] for i in range(0, len(xs), n)]
