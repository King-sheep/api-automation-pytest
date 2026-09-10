# @Author: Sheep Wang
# @File: test_03_order.py
# @Created: 2026-09-08 20:19
# @Description: test_03_order.py


import pytest
from utils.yaml_loader import load_yaml


# load test data
order_test_data = load_yaml("testdata/order_data.yaml")




class TestOrder:
    """Test suite for Order processing."""

    @pytest.mark.parametrize(
        "case", order_test_data, ids=[item["case_title"] for item in order_test_data]
    )
    def test_create_order(self, order_service, case):
        """Data-driven test for order creation endpoint."""
        response = order_service.create_order(case["payload"])
        res_data = response.json()

        assert response.status_code == case["expected_status"]
        assert res_data.get("code") == case["expected_code"]

        if response.status_code == 200:
            assert res_data["data"]["status"] == "PENDING_PAY"