# @Author: Sheep Wang
# @File: payment_service.py
# @Created: 2026-09-07 21:55
# @Description: payment_service.py

from core.client import RestClient




class PaymentService:
    """Encapsulates Transaction Processing and Payment Gateway endpoints."""

    def __init__(self, client: RestClient):
        self.client = client

    def process_payment(self, payment_payload: dict):
        """
        POST /api/v1/payments
        Executes order payment transaction and updates status to PAID.
        """
        return self.client.request("POST", "/api/v1/payments", json=payment_payload)

    def get_payment_info(self, order_id: str):
        """
        GET /api/v1/payments/{order_id}
        Queries transaction details for a specific order.
        """
        return self.client.request("GET", f"/api/v1/payments/{order_id}")