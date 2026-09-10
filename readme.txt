# API Automation Testing Framework

A lightweight, robust, and maintainable REST API test framework built with Python and Pytest.

## 🌟 Key Features

* **Layered Architecture**: Clean 5-layer design (Core, Services, Fixtures, Utils, TestCases) for maximum maintainability.
* **Data-Driven Testing (DDT)**: Complete decoupling of test logic and test data using `@pytest.mark.parametrize` and YAML files.
* **Smart Retry Mechanism**: Uses `pytest-rerunfailures` and custom flaky marks to mitigate network instability and intermittent failures.
* **E2E Dynamic Data Binding**: Real-time extraction and propagation of contextual data (e.g., `order_id`, `amount`) across cross-service workflows.
* **Modern Config**: Single entry configuration via `pyproject.toml`.

## 📁 Project Structure

```text
├── core/            # Base HTTP client and request wrapper
├── services/        # Service object interfaces (Auth, Order, Payment, Product)
├── test_cases/      # Functional & E2E workflow test cases
├── testdata/        # YAML test datasets for DDT
├── utils/           # Yaml loader & Logger helpers
├── conftest.py      # Pytest global fixtures & dependency injection
├── pyproject.toml   # Framework runtime configurations
└── requirements.txt # Project dependencies