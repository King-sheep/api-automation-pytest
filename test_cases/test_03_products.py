# @Author: Sheep Wang
# @File: test_02_product.py
# @Created: 2026-09-08 20:18
# @Description: test_02_product.py


import pytest
from utils.yaml_loader import load_yaml




# Load test data for the products module from YAML file
products_test_data = load_yaml("testdata/products_data.yaml")


class TestProducts:
    """Test suite for Product CRUD operations."""

    @pytest.mark.parametrize(
        "case", products_test_data, ids=[item["case_title"] for item in products_test_data]
    )
    def test_product_crud(self, product_service, case):
        """
        Data-driven test method using explicit action mapping.
        """
        action = case.get("action")
        expected_status = case.get("expected_status")
        expected_code = case.get("expected_code")
        expected_msg = case.get("expected_msg")


        # Dispatch the request dynamically based on the explicit 'action' field in YAML
        if action == "create_product":
            response = product_service.create_product(case["payload"])
        elif action == "get_products":
            response = product_service.query_products(case["payload"])
        elif action == "update_product":
            response = product_service.update_product(case["payload"])
        elif action == "delete_product":
            response = product_service.delete_product(case["payload"])
        else:
            raise ValueError(f"Unsupported action defined in test data: {action}")

        res_data = response.json()  # Result format transfer to Json

        # Assert common status codes
        assert response.status_code == expected_status
        assert res_data.get("code") == expected_code
        assert expected_msg in res_data.get("msg")

        # Additional assertions for successful responses
        if expected_code == 200 and action in ["create_product", "get_products"]:
            assert res_data.get("data") is not None