# Data Analysis Project

This project demonstrates a data cleaning and analysis using Python and Pandas,
It focuses on processing Pokémon data, handling missing values, removing duplicates,forcing 
correct data types, and creating visualizations with a pie chart of the most popular pokemon type.




## Running the project
First install requirements from the **projects** folder using the command:
```bash
pip install -r data_analysis/requirements.txt
```

Next run the code file from the **projects** folder using the command:
```bash
python data_analysis/src/pokemon_analysis.py
```

## Running tests

Make sure to run the test command from the **projects** folder using the command:
```bash
python -m pytest data_analysis/tests
```

## Generating and running test reports 
**Note**: Generating an Allure report requires Allure to be installed on your machine.

Make sure to run the test report commands from the **projects** folder to generate and open the reports, the first 
command will generate the report and the second command runs it

HTML Report:
```bash 
python -m pytest data_analysis/tests --html=data_analysis/reports/report.html --self-contained-html

start data_analysis\reports\report.html
```
---
Allure Report:
```bash 
python -m pytest data_analysis/tests --alluredir=data_analysis/reports/allure-results
 
allure serve data_analysis/reports/allure-results
```


