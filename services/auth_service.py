# @Author: Sheep Wang
# @File: auth_service.py
# @Created: 2026-09-07 21:50
# @Description: auth_service.py


from core.client import RestClient




class AuthService:
    """Encapsulates User Authentication endpoints (Login & Registration)."""

    def __init__(self, client: RestClient):
        self.client = client

    def register(self, payload: dict):
        """
        POST /api/v1/register
        Registers a new user account in the system.
        """
        return self.client.request("POST", "/api/v1/register", json=payload)

    def login(self, payload: dict):
        """
        POST /api/v1/login
        Authenticates user credentials and returns JWT Bearer Token.
        """
        return self.client.request("POST", "/api/v1/login", json=payload)