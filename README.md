# API Automation Testing Framework

A Python-based API automation testing framework built with **Pytest** and the **Requests** library. It demonstrates automated REST API testing against the public [JSONPlaceholder API](https://jsonplaceholder.typicode.com/), including response validation, negative scenarios, reusable client code, and HTML reporting.

## Project Overview

This project demonstrates how to structure and run repeatable API tests, validate HTTP responses and JSON data, and review test results through an HTML report. It also includes a GitHub Actions workflow for automatically executing the tests.

## Technologies Used

- **Python 3.12**
- **Pytest** — test execution and assertions
- **Requests** — HTTP requests
- **pytest-html** — HTML test reports
- **Git and GitHub** — version control and repository hosting
- **GitHub Actions** — continuous integration (CI)

## Features

- GET, POST, PUT, and DELETE API testing
- HTTP status-code validation
- JSON response validation
- Response-field validation
- Negative tests for invalid endpoints and user IDs
- Parameterized tests for multiple test scenarios
- Reusable API client
- Pytest fixtures for configuration
- Self-contained HTML test report generation
- Automated test execution using GitHub Actions

## Project Structure

```text
api-automation-framework/
├── .github/
│   └── workflows/
│       └── api-tests.yml
├── tests/
│   └── test_users.py
├── utils/
│   └── api_client.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

### Key files

- `tests/test_users.py` — contains the API test cases.
- `utils/api_client.py` — provides reusable API-client functionality.
- `conftest.py` — defines shared Pytest fixtures and configuration.
- `pytest.ini` — contains Pytest configuration.
- `.github/workflows/api-tests.yml` — configures automated test execution on GitHub Actions.
- `requirements.txt` — lists the Python dependencies.

## API Under Test

The framework uses **JSONPlaceholder**, a public demo REST API.

Base URL: `https://jsonplaceholder.typicode.com`

The user-related tests use the `/users` resource. JSONPlaceholder is intended for testing and prototyping; write operations such as POST, PUT, and DELETE are simulated rather than persisted like they would be on a production API.

## Installation

### Prerequisites

- Python 3.12 or a compatible Python version
- Git
- Internet access to reach JSONPlaceholder

### 1. Clone the repository

```bash
git clone https://github.com/deepthiwork/api-automation-framework.git
```

### 2. Move into the project directory

```bash
cd api-automation-framework
```

### 3. Create and activate a virtual environment (recommended)

On Windows:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use Command Prompt instead:

```bat
.venv\Scripts\activate.bat
```

### 4. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Make sure `requirements.txt` includes the packages required by the project, including `pytest`, `requests`, and `pytest-html`.

## Run the Tests

Run the full test suite:

```bash
python -m pytest
```

## Generate an HTML Test Report

Run:

```bash
python -m pytest --html=report.html --self-contained-html
```

This creates a self-contained `report.html` file in the current directory. Open it in a web browser to review the results.

## Test Coverage

The project README describes **17 test cases**. The scenarios shown include:

| Test scenario | Purpose |
|---|---|
| GET User | Retrieve user details |
| POST User | Test user creation |
| PUT User | Test updating user details |
| DELETE User | Test user deletion |
| Invalid User | Validate behavior for a non-existent user ID |
| Invalid Endpoint | Validate behavior for an invalid API endpoint |
| JSON Validation | Verify the response content and JSON structure |
| Field Validation | Verify required user fields |
| Parameterized Testing | Exercise multiple valid and invalid user IDs |
| API Client | Exercise reusable API-client configuration |

The exact number and names of test cases depend on the current implementation in `tests/test_users.py`.

## Continuous Integration with GitHub Actions

The workflow at `.github/workflows/api-tests.yml` can run the API tests automatically when code is pushed or a pull request is opened. It can also be started manually using `workflow_dispatch`.

The workflow is configured to:

1. Check out the repository.
2. Set up Python 3.12.
3. Install dependencies from `requirements.txt`.
4. Run the Pytest suite and generate `report.html`.
5. Upload the HTML report as a workflow artifact.

To review a CI run:

1. Open the repository on GitHub.
2. Select the **Actions** tab.
3. Open a workflow run.
4. Review the logs and download **API-Test-Report** from the Artifacts section, if the report was generated and uploaded.

## What This Project Demonstrates

- Writing automated REST API tests in Python
- Using Pytest assertions, fixtures, and parameterization
- Validating status codes and JSON response data
- Organizing reusable API-client code
- Generating readable HTML test reports
- Integrating automated tests into a GitHub Actions workflow

## Repository

[View the project on GitHub](https://github.com/deepthiwork/api-automation-framework)

## Contact

For freelance API testing and automation inquiries, add your preferred professional contact details here.

- **GitHub:** [deepthiwork](https://github.com/deepthiwork)
- **Email:** Add your professional email address
- **Freelance profile:** Add your Upwork, Fiverr, or other portfolio link

---

*This is a portfolio project using a public demo API. Review the repository and test implementation to confirm the exact test count and behavior before presenting those details to clients.*
