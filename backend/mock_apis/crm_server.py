from __future__ import annotations

from fastapi import FastAPI, HTTPException

from ._shared import get_customer_record


app = FastAPI(title="Artha CRM Mock API")


@app.get("/customer/{customer_id}")
def get_customer(customer_id: int) -> dict:
    customer = get_customer_record(customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")

    return {
        "id": customer["id"],
        "name": customer["name"],
        "age": customer["age"],
        "city": customer["city"],
        "kyc": customer["kyc"],
    }
