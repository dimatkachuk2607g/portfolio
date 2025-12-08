# Playwright Automation Project + Github Actions test and report automation

This is a frontend automation project done with Playwright following principles of the POM model
to have clean and scalable code.

I have also created a small website to be used for this project, found under projects/basic_website/src.

Additionally whenever code changes are pushed,
all pytest tests will automatically run in a GitHub Actions
workflow and produce an artifact which contains all reports.


## Running the project
First install requirements from the **projects** folder using the command:
```bash
pip install -r automation_playwright/requirements.txt
```
Next install the browsers using the command:
```bash
playwright install
```

**Note:** By default the project runs with headless mode enabled so you can't see the
execution progress, headless mode can be disabled using the second test command below,
The tests run very quickly so If you want to watch the actions more slowly,
you can temporarily import time and add time.sleep() calls in the test code


Next since the project follows the POM model the automation and tests run side by side
meaning the tests will activate the actual automation,
therefore simply run the tests from the **projects** folder using the commands:
```bash
python -m pytest .\automation_playwright\tests\

python -m pytest .\automation_playwright\tests\ --headed
```

## Generating and running test reports 
**Note**: Generating an Allure report requires Allure to be installed on your machine.

Make sure to run the test report commands from the **projects** folder to generate and open the reports, the first 
command will generate the report and the second command runs it

HTML Report:
```bash 
python -m pytest automation_playwright/tests --html=automation_playwright/reports/report.html --self-contained-html

start automation_playwright\reports\report.html
```
---
Allure Report:
```bash 
python -m pytest automation_playwright/tests --alluredir=automation_playwright/reports/allure-results
 
allure serve automation_playwright/reports/allure-results
```


