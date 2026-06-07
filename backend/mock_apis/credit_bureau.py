from __future__ import annotations

from fastapi import FastAPI, HTTPException

from ._shared import get_customer_record


app = FastAPI(title="Artha Credit Bureau Mock API")


@app.get("/credit-score/{customer_id}")
def get_credit_score(customer_id: int) -> dict:
    customer = get_customer_record(customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")

    return {
        "id": customer["id"],
        "credit_score": customer["credit_score"],
        "scale": 900,
    }
