# PC Builder Project + GitHub Actions Automation



This project allows users to select a PC build (low, mid or high budget) and platform (AMD or Intel).

Loads component details from a JSON file, and prints a summary with full details.

Additionally whenever code changes are pushed,
all pytest tests will automatically run in a GitHub Actions
workflow and produce an artifact which contains all reports.

## Running the project
First install requirements from the **projects** folder using the command:
```bash
pip install -r core_python/requirements.txt
```

Next run the code file from the **projects** folder using the command:
```bash
python core_python/src/pc_builder.py
```

## Running tests

Make sure to run the test command from the **projects** folder using the command:
```bash
python -m pytest core_python/tests
```

## Generating and running test reports 
**Note**: Generating an Allure report requires Allure to be installed on your machine.

Make sure to run the test report commands from the **projects** folder to generate and open the reports, the first 
command will generate the report and the second command runs it

HTML Report:
```bash 
python -m pytest core_python/tests --html=core_python/reports/report.html --self-contained-html

start core_python\reports\report.html
```
---
Allure Report:
```bash 
python -m pytest core_python/tests --alluredir=core_python/reports/allure-results
 
allure serve core_python/reports/allure-results
```


