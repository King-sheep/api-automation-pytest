# @Author: Sheep Wang
# @File: product_service.py
# @Created: 2026-09-07 21:54
# @Description: product_service.py


from core.client import RestClient




class ProductService:
    """Encapsulates Product Catalog and Inventory endpoints."""

    def __init__(self, client: RestClient):
        self.client = client


    def query_products(self, query_payload: dict):
        """
        POST /api/v1/products/query
        Public endpoint to search and filter product catalog.
        """
        return self.client.request("POST", "/api/v1/products/query", json=query_payload)
    

    def create_product(self, product_payload: dict):
        """
        POST /api/v1/products
        Adds a new product to the catalog (Requires Authentication).
        """
        return self.client.request("POST", "/api/v1/products/add", json=product_payload)
    

    def update_product(self, product_payload: dict):
        """
        PUT /api/v1/products
        Updates an existing product's details (Requires Authentication).
        """
        return self.client.request("PUT", "/api/v1/products/update", json=product_payload)
    

    def delete_products(self, product_ids: list[int]):
        """
        DELETE /api/v1/products
        Batch deletes products by ID list (Requires Authentication).
        """
        return self.client.request("DELETE", "/api/v1/products/del", json=product_ids)