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
    token = res_json["data"]["access_token"]
    
    # Inject token into global session headers
    client.set_bearer_token(token)
    log.info("Global authentication successful. Authenticated client ready.")
    
    return client




@pytest.fixture
def auth_service(client):
    return AuthService(client)

@pytest.fixture
def product_service(client):
    return ProductService(client)

@pytest.fixture
def order_service(authenticated_client):
    return OrderService(authenticated_client)

@pytest.fixture
def payment_service(authenticated_client):
    return PaymentService(authenticated_client)