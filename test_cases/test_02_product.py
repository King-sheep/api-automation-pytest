# @Author: Sheep Wang
# @File: test_02_product.py
# @Created: 2026-09-08 20:18
# @Description: test_02_product.py


import pytest
from utils.yaml_loader import load_yaml




# load test data
product_test_data = load_yaml("testdata/product_data.yaml")


class TestProduct:
    """Test suite for Product Catalog management."""

    @pytest.mark.parametrize(
        "case", product_test_data, ids=[item["case_title"] for item in product_test_data]
    )
    def test_product_operations(self, product_service, case):
        """Data-driven test for product query and creation."""
        # Route request based on scenario title
        if "Query" in case["case_title"]:
            response = product_service.query_products(case["payload"])
        else:
            response = product_service.create_product(case["payload"])

        res_data = response.json()
        assert response.status_code == case["expected_status"]
        assert res_data.get("code") == case["expected_code"]