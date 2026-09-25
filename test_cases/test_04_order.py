# @Author: Sheep Wang
# @File: test_03_order.py
# @Created: 2026-09-08 20:19
# @Description: test_03_order.py


import pytest
from utils.yaml_loader import load_yaml




# Load test data for the orders module from YAML file
orders_test_data = load_yaml("testdata/order_data.yaml")


class TestOrders:
    """Test suite for Order CRUD operations (Create, Read, Update, Cancel)."""

    @pytest.mark.parametrize(
        "case", orders_test_data, ids=[item["case_title"] for item in orders_test_data]
    )
    def test_order_crud(self, order_service, case):
        """
        Data-driven test method for order operations using explicit action mapping.
        Leverages authenticated_client automatically via order_service fixture.
        """
        action = case.get("action")
        payload = case.get("payload")
        expected_status = case.get("expected_status")
        expected_code = case.get("expected_code")
        expected_msg = case.get("expected_msg")

        # Route requests dynamically based on the action field in YAML
        if action == "create_order":
            response = order_service.create_order(payload)
        elif action == "query_orders":
            response = order_service.query_orders(payload)
        elif action == "update_order_status":
            response = order_service.update_order_status(payload)
        elif action == "cancel_order":
            response = order_service.cancel_order(payload)
        else:
            pytest.fail(f"Unsupported action: {action}")

        res_data = response.json()

        # Assertions for HTTP status and business response code
        assert response.status_code == expected_status
        assert res_data.get("code") == expected_code
        assert expected_msg in res_data.get("msg")