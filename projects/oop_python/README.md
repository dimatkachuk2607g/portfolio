# Python OOP Character and Warrior Project



This project implements a Character class and a Warrior subclass.  
It includes attributes, methods for attacking, healing, rage attacks, and
use of get/set with private attributes,
There are also tests and test reports for both classes.


## Running the project
First install requirements from the **projects** folder using the command:
```bash
pip install -r oop_python/requirements.txt
```

Next run the code files from the **projects** folder using the following commands,
do note the warrior inherits from character but each file can run independently
```bash
python oop_python/src/character.py

python -m oop_python.src.warrior
```

## Running tests

Make sure to run the test command from the **projects** folder using the command:
```bash
python -m pytest oop_python/tests
```

## Generating and running test reports 
**Note**: Generating an Allure report requires Allure to be installed on your machine.

Make sure to run the test report commands from the **projects** folder to generate and open the reports, the first 
command will generate the report and the second command runs it

HTML Report:
```bash 
python -m pytest oop_python/tests --html=oop_python/reports/report.html --self-contained-html

start oop_python\reports\report.html
```
---
Allure Report:
```bash 
python -m pytest oop_python/tests --alluredir=oop_python/reports/allure-results
 
allure serve oop_python/reports/allure-results
```


