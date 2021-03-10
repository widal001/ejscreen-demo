# EJScreen Demo
Updated example of EJScreen's tool

## Table of Contents

- [About this Project](#overview)
  - [Additional Resources](#additional-resources)
  - [Made With](#made-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## About this Project

This tool provides a demonstration of an updated version of the EJScreen mapping tool, including an API to expose the EJScreen data in a machine readable format.

Below is a brief description of the current EJScreen tool pulled from its [home page](https://www.epa.gov/ejscreen):

>In order to better meet the Agency’s responsibilities related to the protection of public health and the environment, EPA has developed a new environmental justice (EJ) mapping and screening tool called EJSCREEN. It is based on nationally consistent data and an approach that combines environmental and demographic indicators in maps and reports.

To use the EPA's current version of the EJScreen tool and learn more about the underlying dataset, please refer to the links in the Additional Resources section below.

### Additional Resources

- [EJScreen Mapping Tool](https://ejscreen.epa.gov/mapper/)
- [Explanation of EJScreen Indicators](https://www.epa.gov/ejscreen/understanding-ejscreen-results)

### Made With

- [flask](https://flask.palletsprojects.com/en/1.1.x/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [flask restful](https://flask-restful.readthedocs.io/en/latest/)

## Getting Started

### Prerequisites

- Python version 3.6 to 3.8

In order to check which version of python you have installed, run the following command in your command line (for Mac/Linux)

> **NOTE:** in all of the code blocks below, lines preceded with `$` indicate commands you should enter in your command line (excluding the `$` itself), while lines preceded with `>` indicate the expected output from the previous command.

```
$ python --version
> Python 3.7.7
```

If you don't have Python version 3.6 or later installed on your computer, consider using [pyenv](https://github.com/pyenv/pyenv) to install and manage multiple versions of Python concurrently.

### Installation

1. Clone your the repo on your local machine`git clone https://github.com/department-of-general-services/workday-payroll-issues.git`
1. Create a new virtual environment in your project directory `python -m venv env`
1. Activate your virtual environment `source env/bin/activate`
1. Install necessary python packages`pip install -r requirements.txt`
1. Install pre-commit to enable pre-commit hooks (This step ensures that your code is formatted according the Black standard and is compliant with PEP8.)
   ```
   $ pre-commit install
   > pre-commit installed at .git/hooks/pre-commit
   ```
1. Run the tests and make sure everything passes
   ```
   $ pytest
   > =============== XX passed in XXs ===============
   ```
## Usage

1. After you've cloned and installed the repo, start your local test server `python run.py`
1. Open a browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) and you should see `Hello, World.`
1. Additional usage details soon

## Contributing

Details on contributing to the project TBD
