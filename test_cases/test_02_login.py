# @Author: Sheep Wang
# @File: test_02_login.py
# @Created: 2026-09-21 22:22
# @Description: test_02_login.py


import pytest
from utils.yaml_loader import load_yaml

# Load test data for the login module from YAML file
login_test_data = load_yaml("testdata/login_data.yaml")

class TestLogin:
    """Test suite for User Login endpoint."""

    @pytest.mark.parametrize(
        "case", login_test_data, ids=[item["case_title"] for item in login_test_data]
    )
    def test_login(self, auth_service, case):
        """
        Data-driven test method for various login scenarios.
        """
        # Call the encapsulated login method from auth_service
        response = auth_service.login(case["payload"])
        res_data = response.json()

        # Assert HTTP status code and custom business response code
        assert response.status_code == case["expected_status"]
        assert res_data.get("code") == case["expected_code"]

        # Assert msg
        assert case["expected_msg"] in res_data.get("msg", "")

        # If login is successful, verify that the 'token' field exists in the data payload
        if case["expected_code"] == 200:
            data_field = res_data.get("data")
            assert data_field is not None
            assert "token" in data_field