# @Author: Sheep Wang
# @File: test_04_payment.py
# @Created: 2026-09-08 20:19
# @Description: test_04_payment.py


import pytest
from utils.yaml_loader import load_yaml




# Load test data
payment_test_data = load_yaml("testdata/payment_data.yaml")




class TestPayment:
    """Test suite for Payment Gateway processing and End-to-End workflow validation."""

    # Specific retry configuration for flaky payment endpoints (Overrides global settings: 3 retries, 2s delay)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    @pytest.mark.parametrize(
        "case", payment_test_data, ids=[item["case_title"] for item in payment_test_data]
    )
    def test_process_payment(self, payment_service, case):
        """Data-driven test for individual payment processing endpoints."""
        response = payment_service.process_payment(case["payload"])
        res_data = response.json()

        assert response.status_code == case["expected_status"]
        assert res_data.get("code") == case["expected_code"]

    # Retries only when encountering network/connection exceptions (e.g., timeouts), ignoring business assertion failures
    @pytest.mark.flaky(reruns=2, reruns_delay=1, only_rerun="requests.exceptions.RequestException")
    def test_e2e_order_to_payment_workflow(self, order_service, payment_service):
        """
        [E2E Integration Test] Complete order-to-payment business chain.
        1. Create a new order using OrderService.
        2. Extract order_id and total_amount from the response.
        3. Execute payment using PaymentService with the extracted amount.
        4. Verify final order status is updated to PAID via OrderService.
        """
        # Step 1: Create Order
        order_payload = {"items": [{"product_id": 1, "quantity": 2}]}
        create_res = order_service.create_order(order_payload)
        assert create_res.status_code == 200, "Failed to create order in E2E setup"

        order_data = create_res.json()["data"]
        order_id = order_data["order_id"]
        # Dynamically extract total amount calculated by the order service
        total_amount = order_data["total_amount"]

        # Step 2: Pay for Order using the dynamically extracted amount
        payment_payload = {
            "order_id": order_id,
            "payment_method": "CREDIT_CARD",
            "amount": total_amount
        }
        pay_res = payment_service.process_payment(payment_payload)
        assert pay_res.status_code == 200, "Payment failed during E2E flow"
        assert pay_res.json()["data"]["status"] == "SUCCESS"

        # Step 3: Verify Order Payment Status
        order_detail = order_service.get_order_detail(order_id)
        assert order_detail.status_code == 200
        assert order_detail.json()["data"]["status"] == "PAID"