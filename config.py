# @Author: Sheep Wang
# @File: config.py
# @Created: 2026-09-07 21:22
# @Description: config.py


import os


class Settings:
    # Base API Endpoint
    BASE_URL: str = os.getenv("BASE_URL", "http://127.0.0.1:8000")
    
    # Global Request Timeout (in seconds)
    TIMEOUT: int = 10

    # Default Test User Credentials for Authentication
    TEST_USER = {
        "username": "admin",
        "password": "Password123!"
    }


# Singleton instance for easy importing across the project
settings = Settings()