# Projects Folder

This folder contains all **7 hands-on projects** included in my Python QA & Automation portfolio.  
Each project has its own structure, tests, and documentation.


### Recommended Versions and Setup to Avoid Conflicts

- **Python:** 3.13.11
- **PyCharm:** 2025.3
- **Important:** To avoid path/module issues, **mark the `projects` folder as Sources Root** in PyCharm before running any code.


## Quick Setup

To install all requirements for every project at once, from this **projects** folder run:

```bash
pip install -r requirements.txt
```

If you want to run **Playwright** tests, also run:
```bash
playwright install
```

**Browser Note:**  
Tests use Chrome/Chromium by default, **Selenium and Playwright** handle browser drivers automatically in recent versions.
If needed, you can also install Chrome manually to ensure compatibility.
