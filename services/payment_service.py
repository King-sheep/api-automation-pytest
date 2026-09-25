# @Author: Sheep Wang
# @File: payment_service.py
# @Created: 2026-09-07 21:55
# @Description: payment_service.py

from core.client import RestClient




class PaymentService:
    """Encapsulates Payment processing endpoints using GET method."""

    def __init__(self, client: RestClient):
        self.client = client

    def create_payment(self, payload: dict):
        """POST /api/v1/payments - Create a payment."""
        return self.client.request("POST", "/api/v1/payments", json=payload)

    def get_payments_by_order_id(self, order_id: str):
        """GET /api/v1/payments/{order_id} - Retrieve payment records by order ID."""
        return self.client.request("GET", f"/api/v1/payments/{order_id}")