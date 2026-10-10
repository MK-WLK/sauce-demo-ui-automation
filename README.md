# SauceDemo UI Test Automation

[![SauceDemo UI Tests](https://github.com/MK-WLK/sauce-demo-ui-automation/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/MK-WLK/sauce-demo-ui-automation/actions/workflows/tests.yml)

A personal QA automation learning project built to practice web UI testing with **Python, Selenium WebDriver, pytest, and GitHub Actions**.

The project automates selected login, shopping cart, and checkout scenarios on [SauceDemo](https://www.saucedemo.com/). It is a hands-on project for developing my test automation skills and applying concepts such as the Page Object Model, reusable pytest fixtures, assertions, and continuous integration.

**Current test coverage: 16 automated tests.** The test suite has passed locally and on GitHub Actions.

## AI Assistance

Most of the code in this project was generated with AI assistance. I used AI to help implement page objects, tests, browser configuration, and GitHub Actions, while learning through hands-on testing and troubleshooting. I'm still developing my automation skills and use this project to build a better understanding of Selenium, pytest, and CI workflows.

## Tech Stack

- **Python 3.14**
- **Selenium WebDriver** for browser automation
- **pytest** for test execution, fixtures, and assertions
- **Google Chrome** as the browser under test
- **Git and GitHub** for version control
- **GitHub Actions** for automated test execution on pushes and pull requests

## Test Coverage

### Login

Four tests covering:
- Successful login
- Login with an invalid password
- Login with an empty username
- Login with an empty password

### Shopping Cart

Three tests covering:
- Adding one product to the cart
- Adding two products to the cart
- Removing a product from the cart

### Checkout

Nine tests and navigation scenarios covering:
- Navigating from the cart to checkout
- Validation when the first name is missing
- Validation when the last name is missing
- Validation when the postal code is missing
- Proceeding to the checkout overview with valid information
- Verifying the order's product, payment information, shipping information, subtotal, tax, and total
- Completing an order and verifying the confirmation message
- Returning to the inventory page using **Back Home**
- Generating a PDF order and checking that a non-empty PDF file is downloaded

## Project Structure

```text
sauce-demo-ui-automation/
├── .github/
│   └── workflows/
│       └── tests.yml
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── checkout_overview_page.py
│   └── checkout_complete_page.py
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   └── test_cart.py
├── .gitignore
├── requirements.txt
├── README.md
└── SwagLabs-SauceDemo observations.txt
```

## Design and Implementation

### Page Object Model

Page classes keep browser interactions and element locators separate from test cases. The current page objects cover login, inventory, cart, checkout information, checkout overview, and checkout confirmation.

### Reusable pytest fixtures

The `driver` fixture configures and manages the Chrome browser session. The `logged_in_driver` fixture handles standard-user login for tests that require an authenticated session.

### Explicit waits

Explicit waits are used in the page objects to wait for elements to become visible or clickable before interacting with them.

### Isolated browser sessions

Each test receives a fresh browser session through the pytest fixture, helping tests run independently. PDF downloads are directed to pytest's temporary directory rather than the usual Downloads folder.

## Getting Started

### Prerequisites

- Python 3.14
- Google Chrome installed locally
- Git

### 1. Clone the repository

```bash
git clone https://github.com/MK-WLK/sauce-demo-ui-automation.git
cd sauce-demo-ui-automation
```

### 2. Create a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Run the full test suite

```powershell
python -m pytest -v
```

Run only the login tests:

```powershell
python -m pytest tests/test_login.py -v
```

Run the cart and checkout tests:

```powershell
python -m pytest tests/test_cart.py -v
```

## Continuous Integration

The GitHub Actions workflow in `.github/workflows/tests.yml` runs when changes are pushed to `main` or when a pull request targets `main`.

The workflow checks out the repository, sets up Python, installs the project dependencies, and runs the full pytest suite on an Ubuntu runner with headless Chrome.

The current workflow has successfully executed all 16 tests. The badge at the top links to the workflow's latest status and run history.

## Current Limitations and Future Improvements

This is a learning project that is still being developed. Its current limitations include:

- Automated browser coverage is limited to Google Chrome; Firefox and Edge have not been added.
- The test suite covers selected scenarios rather than every possible user flow, validation rule, or edge case.
- The PDF test verifies that a non-empty PDF file is downloaded; it does not inspect the document's contents.
- Dedicated HTML test reports, screenshots on failure, and uploaded CI test artifacts have not been implemented.
- The test suite and page objects may need further refactoring as coverage expands.

Potential next improvements include additional navigation and edge-case tests, improved failure diagnostics, and test report artifacts.

## Learning Goals

This project is helping me gain hands-on experience with:

- Writing maintainable Selenium UI tests in Python
- Using pytest fixtures to share setup and manage browser sessions
- Applying the Page Object Model
- Validating both successful and unsuccessful user flows
- Using Git to create focused commits and manage changes
- Running automated tests through a GitHub Actions CI workflow

The goal is to keep expanding the suite while improving maintainability, reliability, and test coverage.