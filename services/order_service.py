# @Author: Sheep Wang
# @File: order_service.py
# @Created: 2026-09-07 21:51
# @Description: order_service.py


from core.client import RestClient





class OrderService:
    """Encapsulates Order Processing endpoints."""

    def __init__(self, client: RestClient):
        self.client = client

    def create_order(self, order_payload: dict):
        """
        POST /api/v1/orders
        Creates a new purchase order and deducts inventory.
        """
        return self.client.request("POST", "/api/v1/orders", json=order_payload)

    def get_order_detail(self, order_id: str):
        """
        GET /api/v1/orders/{order_id}
        Retrieves detailed information for a specific order.
        """
        return self.client.request("GET", f"/api/v1/orders/{order_id}")