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

![Screen Shot of Home Page](mapper/static/homescreen.png)

This tool provides a demonstration of an updated version of the EJScreen mapping tool, including an API to expose the EJScreen data in a machine readable format.

Below is a brief description of the current EJScreen tool pulled from its [home page](https://www.epa.gov/ejscreen):

> In order to better meet the Agency’s responsibilities related to the protection of public health and the environment, EPA has developed a new environmental justice (EJ) mapping and screening tool called EJSCREEN. It is based on nationally consistent data and an approach that combines environmental and demographic indicators in maps and reports.

To use the EPA's current version of the EJScreen tool and learn more about the underlying dataset, please refer to the links in the Additional Resources section below.

### Additional Resources

- [EJScreen Mapping Tool](https://ejscreen.epa.gov/mapper/)
- [Explanation of EJScreen Indicators](https://www.epa.gov/ejscreen/understanding-ejscreen-results)
- [Project Data Dictionary](docs/data-dictionary.md)

### Made With

- [flask](https://flask.palletsprojects.com/en/1.1.x/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [flask restful](https://flask-restful.readthedocs.io/en/latest/)

## Getting Started

### Prerequisites

- Python version 3.6 to 3.8
- PostgreSQL installed on your computer with a localhost database server created

In order to check which version of python you have installed, run the following in your command line (for Mac/Linux)

> **NOTE:** in all of the code blocks below, lines preceded with `$` indicate commands you should enter in your command line (excluding the `$` itself), while lines preceded with `>` indicate the expected output from the previous command.

```
$ python --version
> Python 3.7.7  # should be something between 3.6.x and 3.8.x
```

If you don't have Python version 3.6 or later installed on your computer, consider using [pyenv](https://github.com/pyenv/pyenv) to install and manage multiple versions of Python concurrently.

In order to check that you have PostgreSQL installed and can connect to the localhost database server, run the following in your command line:

```
$ psql -h localhost  # logs you into the localhost db
> YOUR_USERNAME=#
$ \q  # logs you out of the localhost db
```

If you get an error when trying to connect to the localhost database server, consider using some of these resources to troubleshoot:

- [Getting Started with PostgreSQL on Mac](https://medium.com/@viviennediegoencarnacion/getting-started-with-postgresql-on-mac-e6a5f48ee399)
- [StackOverflow - psql: FATAL: database “user” does not exist](https://stackoverflow.com/questions/17633422/psql-fatal-database-user-does-not-exist)

### Installation

1. Confirm that you have an acceptable version of python installed
   ```
   $ python --version
   > Python 3.7.7  # should be something between 3.6.x and 3.8.x
   ```
1. Confirm that you have PostgreSQL installed on your machine and that you can connect to the localhost database server
   ```
   $ psql -h localhost  # logs you into the localhost db server
   > YOUR_USERNAME=#
   $ \q  # logs you out of the localhost db server
   ```
1. If you encounter errors with either of the first two steps, return to prerequisites before proceeding to step 4
1. Fork the repo following [these instructions](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo)
1. Clone the forked repo on your local machine`git clone https://github.com/YOUR_USERNAME/ejscreen-demo.git`
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

### The App

1. After you've cloned and installed the repo, start your local test server `python run.py`
1. Open a browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) and you should see the home page with links to the original tool and the updated demo.

### The API

1. After you've cloned and installed the repo, start your local test server `python run.py`
1. Open a browser and go to [http://127.0.0.1:5000/api/indicators](http://127.0.0.1:5000/api/indicators) and you should the JSON of all of the indicators in the database.
1. Go to [http://127.0.0.1:5000/api/regions](http://127.0.0.1:5000/api/regions) and you should get the JSON of the first 10 regions from the EJSCREEN source data

## Contributing

Details on contributing to the project TBD
