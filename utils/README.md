# E-Commerce Test Automation Framework

## Overview

This project is a sample end-to-end test automation framework built using Python, Selenium, and Pytest. It demonstrates UI testing, API testing, database validation, integration testing, and CI/CD execution using GitHub Actions.

The framework follows the Page Object Model (POM) design pattern and supports cross-browser execution across Chrome, Firefox, and Edge.

---

## Tech Stack

* Python
* Selenium WebDriver
* Pytest
* Requests
* SQLite
* GitHub Actions
* Allure Reporting

---

## Features

### UI Automation

* Selenium WebDriver
* Page Object Model (POM)
* Explicit Waits
* Cross Browser Testing

  * Chrome
  * Firefox
  * Edge

### Test Framework

* Pytest Framework
* Custom Fixtures
* Custom CLI Parameters
* Test Markers
* Data Driven Testing

### API Testing

* REST API Validation using Requests

### Database Testing

* SQLite Database Validation
* UI + Database Integration Testing

### Reporting & Logging

* HTML Reports
* Allure Reporting
* Screenshot Capture on Failure
* Test Logging

### CI/CD

* GitHub Actions Integration
* Push Validation
* Pull Request Validation
* Scheduled Nightly Execution
* Matrix Strategy for Cross Browser Execution
* Screenshot Artifact Upload
* Dependency Caching

---

## Project Structure

```text
ecom_test/

├── .github/
│   └── workflows/
│       └── regression.yml
│
├── config/
│   └── config.json
│
├── data/
│   ├── product_mapping.py
│   └── test_data.json
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── products_page.py
│   └── cart_page.py
│
├── tests/
│   ├── api_tests/
│   ├── integration_tests/
│   ├── ui_tests/
│   └── conftest.py
│
├── utils/
│   ├── config_reader.py
│   ├── db_utils.py
│   ├── driver_manager.py
│   └── logger.py
│
├── pytest.ini
├── requirements.txt
├── setup_db.py
└── README.md
```

---

## Test Markers

```bash
pytest -m smoke
pytest -m regression
pytest -m ui
pytest -m api
pytest -m db
```

---

## Custom Execution Options

Run tests in Chrome:

```bash
pytest --browser chrome
```

Run tests in Firefox:

```bash
pytest --browser firefox
```

Run tests in Edge:

```bash
pytest --browser edge
```

Run tests in Headless Mode:

```bash
pytest --headless
```

Run Smoke Suite:

```bash
pytest -m smoke --headless
```

Run Regression Suite:

```bash
pytest -m regression --headless
```

---

## CI/CD Workflow

GitHub Actions is configured to:

* Execute Smoke Tests on Push
* Execute Smoke Tests on Pull Requests
* Execute Regression Tests on Scheduled Runs
* Run Tests Across Multiple Browsers
* Upload Failure Screenshots as Artifacts

---

## Sample Test Coverage

### UI Tests

* Login Validation
* Add Product to Cart
* Cart Verification

### API Tests

* Product API Validation

### Integration Tests

* UI Action + Database Verification

---

## Future Enhancements

* Jenkins Integration
* Docker Support
* Parallel Execution
* Advanced Reporting Dashboard
* Cloud Execution (Selenium Grid)

---

## Author

Abhishek Kumar

Automation Framework built for learning and demonstrating real-world QA Automation, API Testing, Database Validation, and CI/CD practices.