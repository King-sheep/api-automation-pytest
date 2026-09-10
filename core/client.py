# @Author: Sheep Wang
# @File: client.py
# @Created: 2026-09-07 21:30
# @Description: client.py



import requests
from config import settings
from utils.logger import log




class RestClient:
    """
    Core HTTP Client wrapper around requests.Session.
    Provides automatic session state management, logging, and uniform request execution.
    """

    def __init__(self, base_url: str = settings.BASE_URL):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def set_bearer_token(self, token: str):
        """
        Injects JWT Bearer token into global headers for subsequent requests.
        Once set, all requests through this client instance will automatically include Authorization.
        """
        self.session.headers.update({"Authorization": f"Bearer {token}"})
        log.info("JWT Bearer token successfully attached to session headers.")

    def request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """
        Generic HTTP request runner.
        
        :param method: HTTP method (GET, POST, PUT, DELETE, etc.)
        :param endpoint: API route endpoint (e.g., '/api/v1/orders')
        :param kwargs: Optional parameters passed to requests (json, params, headers, timeout, etc.)
        :return: requests.Response object
        """
        # Construct full URL
        url = f"{self.base_url}{endpoint}" if not endpoint.startswith("http") else endpoint
        method = method.upper()

        # Set default timeout if not provided
        kwargs.setdefault("timeout", settings.TIMEOUT)

        log.info(f"Sending [{method}] request to: {url}")
        if "json" in kwargs:
            log.info(f"Request Payload (JSON): {kwargs['json']}")
            
        if "params" in kwargs:
            log.info(f"Query Params: {kwargs['params']}")

        try:
            # Execute request using underlying requests.Session
            response = self.session.request(method=method, url=url, **kwargs)
            log.info(f"Response Status Code: {response.status_code}")
            return response

        except requests.RequestException as e:
            log.error(f"HTTP Request failed on [{method}] {url}: {str(e)}")
            raise e