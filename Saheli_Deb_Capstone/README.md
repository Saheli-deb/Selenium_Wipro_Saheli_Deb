**# Wipro Selenium Python Automation Framework**

> **A maintainable, data-driven UI automation framework built with

> Selenium + PyTest + Page Object Model, with reusable utilities,

> failure evidence, structured logging, and HTML reporting.**

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)](https://www.python.org/)

[![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?logo=selenium&logoColor=white)](https://www.selenium.dev/)

[![PyTest](https://img.shields.io/badge/PyTest-Test%20Framework-0A9EDC?logo=pytest&logoColor=white)](https://pytest.org/)

[![Pattern](https://img.shields.io/badge/Design-Page%20Object%20Model-6C5CE7)](#framework-architecture)

[![Status](https://img.shields.io/badge/Test%20Status-10%2F10%20Passed-2EA44F)](#latest-validation)

------------------------------------------------------------------------

**## 1. Executive Summary**

This project is a **production-style Selenium Python automation

framework** created to demonstrate more than simple browser scripting.

The framework separates:

-   ****test intent**** from

-   ****page interaction logic**** from

-   ****test data**** from

-   ****framework configuration**** from

-   ****diagnostic and reporting concerns****.

The result is a test suite that is easier to maintain, extend,

troubleshoot, and reproduce.

**### Application Under Test**

****Automation Exercise****

`https://automationexercise.com/`

The current automation scope covers:

-   Invalid login validation

-   Data-driven product search

-   PyTest-based execution

-   Python `unittest` integration

-   Failure screenshot capture

-   Structured logging

-   HTML execution reporting

------------------------------------------------------------------------

**# 2. Why This Framework?**

A basic Selenium script can automate a click.

A maintainable automation framework should answer much more:

> **Where is the business flow? Where is the UI logic? Where is the

> data? How is failure diagnosed? How can another tester reproduce the

> run?**

This project addresses those concerns through a layered structure.

``` text

                    ┌─────────────────────────┐

                    │       Test Scenarios    │

                    │   PyTest / unittest      │

                    └────────────┬────────────┘

                                 │

                                 ▼

                    ┌─────────────────────────┐

                    │     Page Object Layer   │

                    │ LoginPage / HomePage     │

                    └────────────┬────────────┘

                                 │

                                 ▼

                    ┌─────────────────────────┐

                    │     Base Page Layer     │

                    │ waits / interactions    │

                    └────────────┬────────────┘

                                 │

                                 ▼

                    ┌─────────────────────────┐

                    │      Selenium WebDriver │

                    └────────────┬────────────┘

                                 │

                                 ▼

                    ┌─────────────────────────┐

                    │   Automation Exercise   │

                    └─────────────────────────┘

     Test Data ───────────────► Test Scenarios

     Config ──────────────────► Framework

     Logger ──────────────────► Diagnostics

     Screenshots ─────────────► Failure Evidence

     HTML Report ──────────────► Test Results

```

------------------------------------------------------------------------

**# 3. Framework Architecture**

The framework follows the ****Page Object Model (POM)**** pattern.

**### Layer 1 --- Test Layer**

Contains business-oriented test scenarios.

``` text

tests/

├── test_login.py

├── test_search.py

└── test_unittest_search.py

```

The tests focus on ****what should be validated****, rather than how

individual UI elements are manipulated.

**### Layer 2 --- Page Layer**

``` text

pages/

├── base_page.py

├── login_page.py

└── home_page.py

```

The page layer encapsulates UI interaction.

This prevents locator and browser-interaction logic from being

duplicated throughout test cases.

**### Layer 3 --- Utility Layer**

``` text

utils/

├── config_reader.py

├── csv_reader.py

└── logger.py

```

Reusable framework services are isolated from test logic.

**### Layer 4 --- Data Layer**

``` text

test_data/

├── login_data.csv

└── product_search.csv

```

Test data is externalized so that additional scenarios can be introduced

without rewriting test logic.

**### Layer 5 --- Configuration & Orchestration**

``` text

config/

├── config.ini

conftest.py

pytest.ini

```

This layer controls environment configuration, fixtures, browser

lifecycle, reporting hooks, and test discovery.

------------------------------------------------------------------------

**# 4. Project Structure**

``` text

Saheli_Deb_Capstone/

│

├── pages/

│   ├── __init__.py

│   ├── base_page.py

│   ├── home_page.py

│   └── login_page.py

│

├── tests/

│   ├── __init__.py

│   ├── test_login.py

│   ├── test_search.py

│   └── test_unittest_search.py

│

├── utils/

│   ├── __init__.py

│   ├── config_reader.py

│   ├── csv_reader.py

│   └── logger.py

│

├── config/

│   └── config.ini

│

├── test_data/

│   ├── login_data.csv

│   └── product_search.csv

│

├── screenshots/

│   └── Failure evidence

│

├── reports/

│   ├── automation.log

│   └── test_report.html

│

├── conftest.py

├── pytest.ini

├── requirements.txt

├── README.md

└── venv/

```

> `venv/`, `__pycache__/`, and `.pytest_cache/` are
environment/runtime

> artifacts and should not be committed to source control.

------------------------------------------------------------------------

**# 5. Automated Test Coverage**

**## A. Invalid Login**

****Objective:**** Validate that invalid login combinations are
handled

correctly.

****Implementation:****

-   PyTest

-   Data-driven execution

-   CSV test data

-   Page Object Model

****Test source:****

``` text

tests/test_login.py

```

****Data source:****

``` text

test_data/login_data.csv

```

------------------------------------------------------------------------

**## B. Data-Driven Product Search**

****Objective:**** Validate product search using multiple
independent search

inputs.

****Implementation:****

-   PyTest parametrization/data-driven execution

-   CSV-based test data

-   Page Object Model

-   Explicit synchronization

-   Product-result validation

****Test source:****

``` text

tests/test_search.py

```

****Data source:****

``` text

test_data/product_search.csv

```

Current execution validates ****three product-search datasets****.

------------------------------------------------------------------------

**## C. Unittest Compatibility**

The project also demonstrates interoperability with Python's standard

`unittest` framework.

``` text

tests/test_unittest_search.py

```

This shows that the underlying page-object components can be reused

outside a PyTest-only test style.

------------------------------------------------------------------------

**# 6. Test Execution Lifecycle**

Each automated run follows a controlled lifecycle:

``` text

START

  │

  ▼

Load configuration

  │

  ▼

Initialize browser

  │

  ▼

Launch application

  │

  ▼

Execute test scenario

  │

  ├────────────── PASS ──────────────┐

  │                                  │

  └────────────── FAIL ───────► Capture screenshot

                                     │

                                     ▼

                              Record diagnostic log

                                     │

                                     ▼

  ◄──────────────────────────── Teardown

  │

  ▼

Generate execution report

  │

  ▼

END

```

This lifecycle is centralized through `conftest.py`, reducing
duplicated

setup and teardown code.

------------------------------------------------------------------------

**# 7. Synchronization Strategy**

UI automation should not depend on arbitrary delays.

The framework uses Selenium synchronization mechanisms to wait for the

required application state before continuing.

This is important for:

-   dynamic page loading

-   delayed rendering

-   navigation transitions

-   asynchronously loaded elements

The project avoids using `time.sleep()` as the primary synchronization

mechanism.

------------------------------------------------------------------------

**# 8. Failure Diagnostics**

A failed UI test should provide evidence, not just a red status.

When a test fails, the framework captures:

**### Screenshot**

``` text

screenshots/

```

**### Execution Log**

``` text

reports/automation.log

```

**### PyTest Failure Details**

The terminal output records:

-   failing test

-   source location

-   exception type

-   stack trace

-   execution timing

This makes failures easier to reproduce and investigate.

------------------------------------------------------------------------

**# 9. HTML Reporting**

The framework generates a self-contained HTML test report.

``` text

reports/test_report.html

```

The report provides:

-   execution summary

-   pass/fail status

-   individual test results

-   execution duration

-   Python/platform information

-   plugin information

The latest generated report recorded:

``` text

Total Tests : 6

Passed      : 6

Failed      : 0

Skipped     : 0

Errors      : 0

```

------------------------------------------------------------------------

**# 10. Latest Validation**

The latest successful execution validated ****6 automated tests****:

``` text

✓ test_invalid_login[data0]

✓ test_invalid_login[data1]

✓ test_product_search[product_data0]

✓ test_product_search[product_data1]

✓ test_product_search[product_data2]

✓ TestProductSearch::test_product_search_using_unittest

```

**### Result**

``` text

6 passed

```

This result is also represented in the generated HTML report.

------------------------------------------------------------------------

**# 11. Reproducible Environment**

The project uses a Python virtual environment to isolate project

dependencies.

**### Activate environment --- Windows**

``` powershell

.`\venv`{=tex}`\Scripts`{=tex}`\Activate`{=tex}.ps1

```

**### Install dependencies**

``` bash

python -m pip install -r requirements.txt

```

**### Verify Python**

``` bash

python --version

```

**### Run the complete suite**

``` bash

pytest

```

**### Generate HTML report**

``` bash

pytest --html=reports/test_report.html --self-contained-html

```

------------------------------------------------------------------------

**# 12. Useful Execution Commands**

**### Run all tests**

``` bash

pytest

```

**### Run login tests**

``` bash

pytest tests/test_login.py

```

**### Run product-search tests**

``` bash

pytest tests/test_search.py

```

**### Run unittest-based test**

``` bash

pytest tests/test_unittest_search.py

```

**### Run with HTML reporting**

``` bash

pytest --html=reports/test_report.html --self-contained-html

```

**### Run with verbose output**

``` bash

pytest -v

```

------------------------------------------------------------------------

**# 13. Test Data Strategy**

The framework deliberately separates test data from automation logic.

Example:

``` text

Test Logic

    │

    ▼

CSV Reader

    │

    ▼

login_data.csv / product_search.csv

    │

    ▼

Parameterized Test

```

**### Benefits**

-   Easier maintenance

-   Additional scenarios without code duplication

-   Cleaner test cases

-   Better separation of concerns

-   Easier collaboration

-   Improved scalability for regression testing

------------------------------------------------------------------------

**# 14. Configuration Management**

Environment-specific values are kept outside page/test logic wherever

practical.

``` text

config/config.ini

```

The configuration reader provides a reusable mechanism for accessing

framework configuration.

This design makes it easier to extend the framework for additional

environments such as:

``` text

DEV

QA

STAGING

PRODUCTION-LIKE TEST

```

without redesigning the test layer.

------------------------------------------------------------------------

**# 15. Logging Strategy**

The framework maintains execution logs through the reusable logger

utility.

``` text

utils/logger.py

```

Logs are persisted in:

``` text

reports/automation.log

```

Logging helps distinguish:

-   framework setup problems

-   application navigation problems

-   test failures

-   teardown events

-   screenshot creation

------------------------------------------------------------------------

**# 16. Design Principles Applied**

**### Separation of Concerns**

Test cases, page interactions, data, configuration, and utilities are

kept separate.

**### Reusability**

Common browser interactions are centralized in the base page layer.

**### Maintainability**

UI changes can primarily be handled within page objects instead of every

test case.

**### Data-Driven Testing**

Test inputs are externalized into CSV files.

**### Observability**

Failures produce logs and screenshots rather than only a pass/fail

result.

**### Reproducibility**

Dependencies and execution commands are documented so the environment

can be recreated.

**### Framework Extensibility**

The current structure can support additional pages, scenarios, datasets,

and reporting integrations without restructuring the entire project.

------------------------------------------------------------------------

**# 17. Troubleshooting Playbook**

 
-----------------------------------------------------------------------

  Symptom                             First Checks

  -----------------------------------
-----------------------------------

  `ModuleNotFoundError`               Confirm the active virtual

                                      environment and installed packages

  Browser does not start              Check browser installation and

                                      Selenium environment

  `TimeoutException`                  Inspect locator, page state,

                                      synchronization, and unexpected

                                      overlays

  Element not found                   Validate locator and current page

  Test works manually but fails in    Check timing, overlays, navigation

  automation                          state, and locator stability

  Driver/session problem              Check browser/Selenium environment

                                      and driver management

  Test data not loaded                Validate CSV path, headers,

                                      encoding, and reader utility

  Report not generated                Verify pytest-html installation
and

                                      output path

 
-----------------------------------------------------------------------

------------------------------------------------------------------------

**# 18. Evidence & Quality Artifacts**

The repository contains artifacts intended to make the automation result

auditable:

``` text

Source Code

     +

Test Data

     +

Configuration

     +

Execution Logs

     +

Failure Screenshots

     +

HTML Test Report

     =

Reproducible Automation Evidence

```

The Selenium assignment guidance also emphasizes reproducible

environments, `requirements.txt`, meaningful source comments, and

execution evidence. This project therefore keeps those concerns visible

in the repository rather than treating the final test result as the only

deliverable.

------------------------------------------------------------------------

**# 19. Extensibility Roadmap**

The current framework is intentionally structured so additional

engineering capabilities can be introduced incrementally.

Potential next extensions include:

-   Cross-browser execution

-   Environment-specific configuration

-   Parallel execution

-   Retry strategy for infrastructure-level failures

-   Allure/advanced reporting

-   CI/CD execution

-   Screenshot embedding into reports

-   API + UI hybrid validation

-   Additional Page Object modules

-   Expanded regression suites

-   Test tagging such as smoke/regression

-   Remote browser execution

These are extension points rather than claims about features already

implemented.

------------------------------------------------------------------------

**# 20. Engineering Takeaway**

The objective of this project is not simply to demonstrate that Selenium

can open a browser.

It demonstrates a more complete automation mindset:

``` text

     AUTOMATION

          │

          ├── Maintainability

          ├── Reusability

          ├── Data Separation

          ├── Synchronization

          ├── Diagnostics

          ├── Reporting

          └── Reproducibility

```

The framework turns individual Selenium scripts into a structured test

system that can be extended as application coverage grows.

------------------------------------------------------------------------

**## Author**

****Saheli Deb****

****Project:**** Wipro Selenium Python Automation Capstone

****Technology Focus:**** Python • Selenium WebDriver • PyTest •
Page Object

Model • Test Automation • Data-Driven Testing

------------------------------------------------------------------------

**## License**

This project is intended for educational and portfolio demonstration

## purposes.

# 21. Recent Feature Additions

The framework was extended with two important end-to-end UI automation
areas:

-   **User Registration / Signup**
-   **Shopping Cart Management**

These additions extend the project from authentication and
product-search validation into realistic e-commerce user workflows.

------------------------------------------------------------------------

## 21.1 User Registration / Signup Automation

### Objective

Validate the complete new-user registration workflow on Automation
Exercise.

### Automated Flow

``` text
Open Application
      |
      v
Navigate to Signup / Login
      |
      v
Enter Name + Email
      |
      v
Submit Signup
      |
      v
Fill Account Information
      |
      v
Fill Address / User Details
      |
      v
Create Account
      |
      v
Validate "ACCOUNT CREATED!"
      |
      v
Continue
      |
      v
Validate Logged-In State
```

### Validation Strategy

The signup test does not rely only on the URL changing. It validates
visible application state after registration, which makes the assertion
closer to an actual user-facing outcome.

The test verifies that:

-   the registration form can be completed;
-   the account creation flow reaches the expected success state;
-   the user can continue after account creation;
-   the application displays the logged-in state after successful
    registration.

### Test Source

``` text
tests/test_signup.py
```

### Page Object

``` text
pages/signup_page.py
```

The page object contains the locators and reusable actions required by
the registration workflow, keeping browser interaction logic outside the
test case.

------------------------------------------------------------------------

## 21.2 Shopping Cart Automation

### Objective

Validate core shopping-cart operations after selecting a product.

The cart module currently covers:

1.  Add product to cart
2.  Open cart
3.  Verify cart contents
4.  Increase product quantity
5.  Verify updated quantity
6.  Remove product from cart
7.  Verify product removal

### Automated Flow

``` text
Open Products
      |
      v
Find Product
      |
      v
Add Product to Cart
      |
      v
Open Cart
      |
      v
Validate Product
      |
      +----------------------+
      |                      |
      v                      v
Increase Quantity       Remove Product
      |                      |
      v                      v
Validate Quantity      Validate Removal
```

### Test Source

``` text
tests/test_cart.py
```

### Page Object

``` text
pages/cart_page.py
```

The cart page object centralizes cart-specific locators and actions so
that the test cases remain focused on business behaviour rather than
Selenium implementation details.

------------------------------------------------------------------------

## 21.3 Add Product to Cart

The add-to-cart scenario validates that a selected product can be added
successfully from the products interface.

The automation identifies the requested product by name and interacts
with its corresponding **Add to cart** control.

The flow then opens the cart and validates that the expected product is
present.

### Example Scenario

``` text
Product: Blue Top

Products Page
     |
     v
Locate "Blue Top"
     |
     v
Click "Add to cart"
     |
     v
Open Cart
     |
     v
Verify "Blue Top" exists
```

This demonstrates product-specific interaction rather than depending on
a fixed screen position.

------------------------------------------------------------------------

## 21.4 Product Quantity Validation

The cart test suite also validates quantity changes.

### Scenario

``` text
Add Product
     |
     v
Open Cart
     |
     v
Read Initial Quantity
     |
     v
Increase Quantity
     |
     v
Read Updated Quantity
     |
     v
Assert Updated Quantity
```

This verifies that the cart reflects the expected quantity after the
user changes the number of items.

The test is designed around observable cart state instead of simply
asserting that a button was clicked.

------------------------------------------------------------------------

## 21.5 Remove Product from Cart

The remove-product scenario validates that a product can be removed from
the shopping cart.

### Flow

``` text
Add Product
     |
     v
Open Cart
     |
     v
Locate Product Row
     |
     v
Click Remove
     |
     v
Wait for Cart Update
     |
     v
Verify Product Is No Longer Present
```

This validates the resulting application state after the removal
operation.

------------------------------------------------------------------------

## 21.6 Robust Selenium Interaction for Dynamic UI

During implementation, the Automation Exercise site was observed to
contain advertisement overlays that can interfere with Selenium clicks.

The framework was therefore strengthened to handle common UI-interaction
problems such as:

-   advertisement iframes covering controls;
-   click interception;
-   dynamically rendered elements;
-   delayed navigation;
-   asynchronous cart updates.

The page objects use explicit waits and, where appropriate, a controlled
JavaScript click fallback when a normal Selenium click is intercepted.

Advertisement handling is isolated from the business test flow so that
the test cases remain readable.

### Interaction Strategy

``` text
Locate Element
      |
      v
Wait Until Usable
      |
      v
Normal Selenium Click
      |
      +------ Success ------> Continue
      |
      +------ Intercepted
                    |
                    v
              Handle Overlay
                    |
                    v
              Retry Interaction
```

This approach was particularly useful for the product and cart workflows
where advertisement overlays could otherwise cause
`ElementClickInterceptedException` or `TimeoutException`.

------------------------------------------------------------------------

## 21.7 Updated Page Object Responsibilities

The current page-object layer now includes additional responsibilities:

``` text
pages/
│
├── base_page.py
│   └── Common waits and browser interactions
│
├── home_page.py
│   ├── Product navigation
│   ├── Product search
│   └── Product selection / cart entry point
│
├── login_page.py
│   └── Login interactions and validation
│
├── signup_page.py
│   └── User registration and account-creation flow
│
└── cart_page.py
    ├── Open cart
    ├── Validate cart
    ├── Read quantity
    ├── Increase quantity
    └── Remove product
```

This keeps each page object's responsibility focused and makes future UI
changes easier to maintain.

------------------------------------------------------------------------

## 21.8 Updated Test Suite

The project now includes the following major test areas:

  ---------------------------------------------------------------------------------
  Test Area               Test File                         Coverage
  ----------------------- --------------------------------- -----------------------
  Invalid Login           `tests/test_login.py`             Invalid credential
                                                            validation

  Product Search          `tests/test_search.py`            Data-driven product
                                                            search

  Unittest Search         `tests/test_unittest_search.py`   PyTest/unittest
                                                            compatibility

  User Signup             `tests/test_signup.py`            Account creation and
                                                            logged-in state

  Shopping Cart           `tests/test_cart.py`              Add, quantity update,
                                                            and removal
  ---------------------------------------------------------------------------------

The cart test module contains three focused scenarios:

``` text
test_add_product_to_cart
test_increase_product_quantity
test_remove_product_from_cart
```

------------------------------------------------------------------------

## 21.9 Latest Validation

The complete suite was executed using:

``` bash
pytest -v
```

The latest validation completed with:

``` text
10 passed
```

The successful execution covered the existing login/search/unittest
scenarios together with the newly added signup and cart scenarios.

A typical successful run includes:

``` text
test_cart.py::test_add_product_to_cart             PASSED
test_cart.py::test_increase_product_quantity      PASSED
test_cart.py::test_remove_product_from_cart       PASSED

test_login.py::test_invalid_login[...]             PASSED
test_search.py::test_product_search[...]           PASSED
test_signup.py::test_user_signup                   PASSED
test_unittest_search.py::...                       PASSED
```

------------------------------------------------------------------------

## 21.10 Engineering Value of the New Features

The new workflows demonstrate several important Selenium automation
concepts:

-   **End-to-end workflow automation**
-   **Page Object Model expansion**
-   **Reusable page methods**
-   **Explicit synchronization**
-   **Dynamic element handling**
-   **Advertisement/overlay handling**
-   **State-based assertions**
-   **Cart data validation**
-   **Negative and positive workflow validation**
-   **Separation of test logic from UI interaction logic**

The project therefore moves beyond isolated Selenium actions and
demonstrates realistic e-commerce regression testing.

------------------------------------------------------------------------
