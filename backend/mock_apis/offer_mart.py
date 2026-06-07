from __future__ import annotations

from fastapi import FastAPI, HTTPException

from ._shared import get_customer_record


app = FastAPI(title="Artha Offer Mart Mock API")


@app.get("/offers/{customer_id}")
def get_offer(customer_id: int) -> dict:
    customer = get_customer_record(customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")

    return {
        "id": customer["id"],
        "pre_approved_limit": customer["pre_approved_limit"],
        "currency": "INR",
    }
