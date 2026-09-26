# Assignment 8 – Data-Driven Automation (DDT)

The test reads multiple username/password combinations from CSV and executes the same login flow for every row.

Expected CSV columns:
username,password,expected

For this demo:
- standard_user / secret_sauce -> success
- invalid combinations -> login error

Run:
pytest -v test_login_ddt.py
