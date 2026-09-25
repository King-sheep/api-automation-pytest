# @Author: Sheep Wang
# @File: conftest.py
# @Created: 2026-09-07 21:42
# @Description: conftest.py


import pytest
from config import settings
from core.client import RestClient
from utils.logger import log


from services.auth_service import AuthService
from services.product_service import ProductService
from services.order_service import OrderService
from services.payment_service import PaymentService




@pytest.fixture(scope="session")
def client():
    """
    Provides a clean, unauthenticated RestClient instance for public endpoints
    such as Registration or Login.
    Scope='session' ensures only one client is instantiated for the entire test run.
    """
    log.info("Initializing public RestClient instance...")
    return RestClient(base_url=settings.BASE_URL)


@pytest.fixture(scope="session")
def authenticated_client(client):
    """
    Automates user authentication before executing protected test suites.
    1. Sends a login request using default credentials from settings.
    2. Extracts JWT token from the response.
    3. Injects token into RestClient session.
    4. Returns authenticated client instance ready for protected requests.
    """
    log.info("Executing global login fixture to obtain Bearer Token...")
    
    login_payload = {
        "username": settings.TEST_USER["username"],
        "password": settings.TEST_USER["password"]
    }
    
    response = client.request("POST", "/api/v1/login", json=login_payload)
    
    # Verify login succeeded in fixture setup
    assert response.status_code == 200, f"Global login fixture failed! Response: {response.text}"
    
    res_json = response.json()
    token = res_json["data"]["token"]
    
    # Inject token into global session headers
    client.set_bearer_token(token)
    log.info("Global authentication successful. Authenticated client ready.")
    
    return client



# 
@pytest.fixture
def auth_service(client):
    return AuthService(client)

@pytest.fixture
def product_service(authenticated_client):
    return ProductService(authenticated_client)

@pytest.fixture
def order_service(authenticated_client):
    return OrderService(authenticated_client)

@pytest.fixture
def payment_service(authenticated_client):
    return PaymentService(authenticated_client)



# Create temporary_order for payment cases =========================================================================
@pytest.fixture
def temporary_order(order_service):
    """
    Fixture that automatically creates an order and extracts 
    its order_id and total_amount for downstream payment tests.
    """
    # 1. Prepare payload for creating a single order
    payload = {
        "items": [
            {"product_id": 1, "quantity": 1}
        ]
    }
    
    # 2. Call order service to create order
    response = order_service.create_order(payload)
    res_data = response.json()
    
    # 3. Extract order_id and total_amount from the newly upgraded API response
    order_data = res_data.get("data", {})
    order_id = order_data.get("order_id")
    total_amount = order_data.get("total_amount")
    
    # 4. Yield them as a dictionary to the test function
    yield {
        "order_id": order_id,
        "amount": total_amount
    }