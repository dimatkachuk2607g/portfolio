# Python API Automation Project using Requests, Pytest, and Postman

This project contains pytest functions for testing the JSONPlaceholder API,
It uses CRUD operations alongside the requests library to automate API testing.

additionally includes a conftest file that can share fixtures to multiple
pytest files, and the Postman collection used to visualize the responses.

## Running the project
First install requirements from the **projects** folder using the command:
```bash
pip install -r api_testing/requirements.txt
```
Next, since this is an API testing project, running the project simply means executing the
tests using the command in the following section.
## Running tests

Make sure to run the test command from the **projects** folder using the command:
```bash
python -m pytest api_testing/tests
```

## Generating and running test reports 
**Note**: Generating an Allure report requires Allure to be installed on your machine.

Make sure to run the test report commands from the **projects** folder to generate and open the reports, the first 
command will generate the report and the second command runs it

HTML Report:
```bash 
python -m pytest api_testing/tests --html=api_testing/reports/report.html --self-contained-html

start api_testing\reports\report.html
```
---
Allure Report:
```bash 
python -m pytest api_testing/tests --alluredir=api_testing/reports/allure-results
 
allure serve api_testing/reports/allure-results
```


