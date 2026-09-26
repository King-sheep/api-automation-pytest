# 🚀 E-Commerce API Automation Testing Framework

> An industrial-grade, data-driven API automation testing framework built with **Python**, **Pytest**, **FastAPI**, and **GitHub Actions**, featuring dynamic interface dependency chaining and automated CI/CD reporting.

---

## ✨ Key Features

* **Dynamic Data Chaining**: Solves the classic automation pain point by implementing dynamic test dependencies (e.g., automatically capturing and injecting newly created `order_id` and total amount into downstream payment test cases via Pytest fixtures).
* **Data-Driven Architecture**: Complete decoupling of test data and test scripts using structured **YAML** files and **Pydantic** models.
* **Comprehensive Test Reporting**: Integrated with `pytest-html` to generate clean, self-contained, and professional HTML test reports automatically.
* **Continuous Integration (CI/CD)**: Fully automated testing pipelines configured with **GitHub Actions**, ensuring seamless regression testing on every code push.
* **Professional Engineering Standards**: Clean project architecture following MVC/DAO design patterns, with standardized English code annotations and documentation across the entire codebase.

---

## 🛠️ Tech Stack

* **Core Language**: Python 3.10+
* **Test Framework**: Pytest, Pytest-HTML, Pytest-RerunFailures
* **Mock / API Backend**: FastAPI, Pydantic, SQLAlchemy, SQLite
* **Data Management**: PyYAML, Requests
* **CI/CD & DevOps**: GitHub Actions

---

## 📂 Project Structure

```text
api-automation-pytest/
│
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI/CD pipeline configuration
├── dao/                    # Data Access Object layer for backend database operations
├── models/                 # Pydantic data models and schemas
├── services/               # Business logic and API request encapsulation layer
├── test_cases/             # Pytest test suites (Data-driven test execution)
│   ├── test_01_auth.py
│   ├── test_02_login.py
│   ├── test_03_products.py
│   ├── test_04_order.py
│   └── test_05_payment.py  # Core payment test suite with dynamic order chaining
├── testdata/               # YAML test data configuration files
├── utils/                  # Helper utilities (YAML loader, logger, etc.)
├── conftest.py             # Global Pytest fixtures and dynamic dependency hooks
├── requirements.txt        # Project dependencies
└── README.md