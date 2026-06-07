from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "customers.json"


@lru_cache(maxsize=1)
def load_customers() -> list[dict[str, Any]]:
    with DATA_PATH.open("r", encoding="utf-8") as file_handle:
        return json.load(file_handle)


def get_customer_record(customer_id: int) -> dict[str, Any] | None:
    for customer in load_customers():
        if int(customer["id"]) == customer_id:
            return customer
    return None
