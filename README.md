# CAPSTONE PROJECT 2 
## SAHELI DEB -- 12023052019071
## video link https://drive.google.com/file/d/1chC_bbRtW4101y7IZOzxt53f_ztz-0j2/view?usp=sharing
A structured **Selenium automation and testing repository** containing a complete capstone automation framework, Selenium lab work, training exercises, API/BDD-related practice, Robot Framework work, and supporting certificates.

This repository brings together the practical work completed during Selenium/Web Automation training in one organized place.

---

## 📌 Repository Overview

The repository is organized into three major sections:

| Folder | Purpose |
|---|---|
| `Saheli_Deb_Capstone/` | Main Selenium Python automation capstone project |
| `Lab_Work/` | Selenium and automation training exercises, assignments, and practice work |
| `Certificates/` | Training/course completion certificates and supporting documents |

The repository is intended to demonstrate both **framework development** and **hands-on automation testing practice**.

---

# 🏗️ Repository Structure

```text
Selenium_Wipro_Saheli_Deb/
│
├── Saheli_Deb_Capstone/
│   ├── config/
│   ├── core/
│   ├── pages/
│   ├── reports/
│   ├── screenshots/
│   ├── test_data/
│   ├── tests/
│   ├── utils/
│   ├── conftest.py
│   ├── pytest.ini
│   ├── requirements.txt
│   ├── README.md
│   └── .gitignore
│
├── Lab_Work/
│   └── Selenium / automation training exercises
│
├── Certificates/
│   └── Training and supporting certificates
│
└── .gitignore
```

---

# 🚀 1. Saheli_Deb_Capstone

The `Saheli_Deb_Capstone` folder contains the primary automation project.

It is a **Python + Selenium + PyTest Page Object Model (POM)** based framework designed around maintainability, reusable components, test data, logging, screenshots, and HTML reporting.

### Main technologies

- Python 3.9
- Selenium WebDriver
- PyTest
- Page Object Model (POM)
- Chrome WebDriver
- HTML test reporting
- Data-driven testing
- Explicit waits
- Reusable automation utilities
- Structured logging
- Failure screenshots

### Current automated coverage

The capstone currently includes automation around:

- User signup
- Invalid login validation
- Product search
- Product search using parameterized test data
- Add product to cart
- Increase product quantity
- Remove product from cart
- Additional search validation through reusable test structures

The test suite is organized so that application interaction remains inside page classes while test files focus on **test scenarios and assertions**.

---

# 🧩 2. Page Object Model

The capstone follows the **Page Object Model** design pattern.

Instead of placing Selenium locators and browser operations directly inside every test, application pages are represented as reusable Python classes.

Example structure:

```text
pages/
├── base_page.py
├── home_page.py
├── login_page.py
├── signup_page.py
└── cart_page.py
```

### BasePage

`BasePage` provides reusable Selenium operations and common framework functionality.

This avoids repeating browser interaction logic throughout individual page classes.

Typical responsibilities include:

- Element interaction
- Explicit waiting
- URL handling
- Browser-related helper operations
- Reusable Selenium utilities

### HomePage

Handles homepage/product-related functionality such as:

- Opening the Products page
- Searching for products
- Validating search results
- Counting returned products
- Adding a selected product to the cart

The implementation also contains handling for advertisement iframes that can interfere with Selenium clicks.

### LoginPage

Contains login-related page operations and validation for login scenarios.

### SignupPage

Contains registration-related operations and user signup flow handling.

### CartPage

Contains cart-related operations including:

- Cart visibility validation
- Product quantity handling
- Product removal
- Cart-related assertions

---

# 🧪 3. Test Suite

The automated tests are located inside:

```text
tests/
```

Current test modules include:

```text
tests/
├── test_cart.py
├── test_login.py
├── test_search.py
├── test_signup.py
└── test_unittest_search.py
```

### Test organization

The test layer is responsible for:

1. Starting the required page objects.
2. Executing a business scenario.
3. Calling reusable page methods.
4. Validating expected results through assertions.
5. Producing test execution results through PyTest.

This separation keeps the framework easier to maintain and extend.

---

# 📊 4. Data-Driven Testing

The project uses test data to avoid hard-coding every scenario directly into the test logic.

This makes it possible to execute similar scenarios with different inputs.

For example, product search tests can be parameterized with multiple product names.

Conceptually:

```text
Test Case
   │
   ├── Product A
   ├── Product B
   └── Product C
```

The same test logic can therefore validate multiple input combinations.

---

# ⏳ 5. Explicit Wait Strategy

The framework uses Selenium's explicit wait mechanism through:

```python
WebDriverWait
```

and Selenium expected conditions.

This is important because modern websites frequently load elements dynamically.

Instead of depending on fixed delays such as:

```python
time.sleep(5)
```

the framework can wait for a meaningful browser condition such as:

```python
EC.visibility_of_element_located(...)
```

or:

```python
EC.element_to_be_clickable(...)
```

This improves synchronization between the automation script and the web application.

---

# 🛡️ 6. Advertisement / Click Interception Handling

The Automation Exercise application may display advertisement iframes that can overlap with Selenium elements.

The capstone therefore includes an advertisement-handling approach.

The framework can hide known advertisement iframe elements before attempting critical interactions.

Where appropriate, the automation also provides a JavaScript click fallback when a normal Selenium click is intercepted.

The intended flow is:

```text
Locate element
      ↓
Check visibility / clickability
      ↓
Attempt normal Selenium click
      ↓
If click is intercepted
      ↓
Handle advertisement overlay
      ↓
Retry interaction
```

This was added to make product/search/cart interactions more reliable.

---

# 📝 7. Logging

The framework contains structured logging support.

Logging helps track important execution events such as:

```text
Browser started
Headless mode configured
Implicit wait configured
Application launched
Test failure
Screenshot saved
Browser closed
```

Logs are useful for debugging failures without having to manually reproduce every test step.

---

# 📸 8. Failure Screenshots

When a test fails, the framework captures a screenshot.

Screenshots are stored under:

```text
screenshots/
```

For example:

```text
screenshots/
├── test_add_product_to_cart.png
├── test_increase_product_quantity.png
├── test_remove_product_from_cart.png
└── ...
```

This provides visual evidence of the browser state at the time of failure.

---

# 📄 9. HTML Test Reporting

PyTest HTML reporting is configured for test execution.

The generated report provides a consolidated view of:

- Test cases
- Pass/fail status
- Execution information
- Failure details
- Test duration

Reports are maintained under:

```text
reports/
```

This makes the project suitable for demonstrating structured test execution rather than only terminal-based results.

---

# 🔧 10. Configuration

Framework configuration is separated from test implementation.

Important files include:

```text
config/
├── config.ini
```

and:

```text
pytest.ini
```

This keeps environment/test configuration separate from page objects and test cases.

---

# 🧰 11. Utility Layer

Reusable helper functionality is maintained under:

```text
utils/
```

Current utility areas include:

- Configuration reading
- CSV/data reading
- Logging

This follows the principle of keeping common functionality reusable instead of duplicating it across test cases.

---

# 🧪 12. Test Execution

Activate the project virtual environment first.

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

Then run the complete test suite:

```powershell
pytest -v
```

Run a particular test file:

```powershell
pytest tests/test_cart.py -v
```

Run a specific test:

```powershell
pytest tests/test_cart.py::test_add_product_to_cart -v
```

---

# 📦 13. Dependencies

The capstone dependencies are maintained in:

```text
requirements.txt
```

Install them using:

```powershell
pip install -r requirements.txt
```

The project uses the Python virtual environment:

```text
venv/
```

The virtual environment itself should not be committed to source control.

---

# 🔄 14. Typical Automation Flow

A typical test follows this architecture:

```text
                    ┌─────────────────────┐
                    │      PyTest Test    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Page Object      │
                    │       Class         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     BasePage        │
                    │ Reusable Selenium   │
                    │     Operations      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Selenium WebDriver  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Web Application   │
                    └─────────────────────┘
```

Supporting components work alongside this flow:

```text
Test Data ───────────────┐
                         │
Configuration ───────────┤
                         ▼
                    Test Execution
                         │
Logging ─────────────────┤
                         │
Screenshots ─────────────┤
                         │
HTML Report ─────────────┘
```

---

# 📚 15. Lab_Work

The `Lab_Work` directory contains additional practical automation and testing work completed during training.

This section is kept separate from the capstone so that:

- Training exercises remain organized.
- Individual assignments can be reviewed independently.
- The main capstone remains focused on the framework implementation.
- Different automation concepts can be demonstrated without mixing them into the production-style project structure.

The repository also contains work related to areas such as Selenium training, API/BDD exercises, and Robot Framework practice.

---

# 🎓 16. Certificates

The `Certificates` directory contains supporting certificates associated with the training and learning activities represented in this repository.

These documents provide supporting evidence for the learning and practical work included alongside the automation projects.

---

# 🧠 17. Key Concepts Demonstrated

This repository demonstrates practical understanding of:

### Selenium

- WebDriver
- Locators
- Element interaction
- Explicit waits
- Dynamic element handling
- Browser automation
- Click interception handling

### PyTest

- Test discovery
- Assertions
- Fixtures
- Parameterized testing
- Test organization
- HTML reporting

### Framework Design

- Page Object Model
- Base page abstraction
- Reusable utilities
- Configuration management
- Data-driven testing
- Logging
- Failure evidence

### Testing Practices

- Positive test scenarios
- Negative test scenarios
- Functional UI validation
- Regression-style test execution
- Failure investigation
- Screenshot-based debugging

---

# 📈 18. Current Validation

The capstone test suite has been executed using:

```powershell
pytest -v
```

with the current suite completing successfully:

```text
10 passed
```

The successful execution covers the currently implemented cart, login, search, signup, and related search test scenarios.

---

# 🔮 19. Future Extensions

The framework can be extended with additional automation capabilities such as:

- Checkout flow automation
- Order placement validation
- Product category filtering
- More extensive data-driven scenarios
- API integration testing
- CI/CD execution
- Cross-browser execution
- Parallel test execution
- Enhanced reporting
- Allure reporting
- Jenkins/GitHub Actions integration

These are potential extensions and are not represented as currently implemented functionality unless present in the corresponding project files.

---

# 👩‍💻 Author

**Saheli Deb**

Selenium Automation | Python | PyTest | Page Object Model

---

# 📌 Repository Purpose

This repository serves as a consolidated portfolio of Selenium and automation testing work, combining:

```text
Training
   +
Hands-on Lab Work
   +
Automation Framework Development
   +
Testing Practice
   +
Supporting Certificates
```

The primary goal is to demonstrate the transition from individual Selenium exercises to a structured, reusable, maintainable automation framework.

---

## ⭐ Technology Stack

```text
Python
Selenium WebDriver
PyTest
Page Object Model
ChromeDriver
HTML Reporting
Logging
Data-Driven Testing
Git / GitHub
```

---

## 📄 License

This repository is primarily intended for educational, training, demonstration, and portfolio purposes.
