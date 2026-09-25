# @Author: Sheep Wang
# @File: test_04_payment.py
# @Created: 2026-09-08 20:19
# @Description: test_04_payment.py


import pytest
from utils.yaml_loader import load_yaml

payment_test_data = load_yaml("testdata/payment_data.yaml")

class TestPayment:
    """Test suite for Payment service with interface dependency chaining."""

    @pytest.mark.parametrize(
        "case", payment_test_data, ids=[item["case_title"] for item in payment_test_data]
    )
    def test_payment_operations(self, payment_service, temporary_order, case):
        """
        Data-driven test method handling both POST create_payment 
        and GET get_payments_by_order_id with dynamic order dependency.
        """
        action = case.get("action")
        payload = case.get("payload", {}).copy()
        
        # Handle dynamic order ID injection from the fixture
        if case.get("need_dynamic_order"):
            # Inject the freshly created order_id into the request payload
            payload["order_id"] = temporary_order["order_id"]
            
            # Align the total amount automatically for payment creation actions
            if action == "create_payment":
                current_amount = payload.get("amount")
                if "payment_amount" not in payload:
                    payload["payment_amount"] = temporary_order["amount"]

        expected_status = case.get("expected_status")
        expected_code = case.get("expected_code")
        expected_msg = case.get("expected_msg")

        # Route requests dynamically based on the action defined in YAML
        if action == "create_payment":
            # POST /api/v1/payments
            response = payment_service.create_payment(payload)
            
        elif action == "get_payments_by_order_id":
            # GET /api/v1/payments/{order_id} using path parameter splicing
            order_id = payload.get("order_id")
            response = payment_service.get_payments_by_order_id(order_id)
            
        else:
            pytest.fail(f"Unsupported action: {action}")

        res_data = response.json()

        # Assertions for HTTP status and business response code
        assert response.status_code == expected_status
        assert res_data.get("code") == expected_code
        assert expected_msg in res_data.get("msg")