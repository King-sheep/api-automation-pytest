# @Author: Sheep Wang
# @File: test_01_auth.py
# @Created: 2026-09-08 20:17
# @Description: test_01_auth.py


import pytest
from utils.yaml_loader import load_yaml




# load test data
auth_test_data = load_yaml("testdata/auth_data.yaml")


class TestAuth:
    """Test suite for User Authentication endpoints (Login & Registration)."""

    @pytest.mark.parametrize(
        "case", auth_test_data, ids=[item["case_title"] for item in auth_test_data]
    )
    def test_login(self, auth_service, case):
        """Data-driven test for login endpoint."""
        response = auth_service.register(case["payload"])
        res_data = response.json()

        assert response.status_code == case["expected_status"]
        assert res_data.get("code") == case["expected_code"]