# Assignment 9 – PyTest Integration with HTML Reporting

Features:
- PyTest fixture for browser setup and teardown
- Login validation
- Automatic screenshot on test failure
- pytest-html execution report

Run:
pytest -v --html=reports/report.html --self-contained-html

The screenshot hook stores failure screenshots in screenshots/.
