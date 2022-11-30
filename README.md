# python-concepts
## Installation
- Python was already installed on my Mac as `python3`
- Poetry is installed using homebrew
- Pytest is installed using Poetry

## Python Command Line
- `python3 --version` checks version of python
- `pip3 --version` checks version of pip
- `python3 hello.py` runs the `hello.py` script
- `poetry run python hello.py` runs a Python script in `poetry` environment

## Pytest Command Line
- `pytest -h` to see all the command line options
- `pytest -v` is verbose, will give you more details
- `pytest -s` show output of print() statements
- `pytest -vs` combine `-v` and `-s` for verbose and print() output
- `pytest -rP` shows the captured output of passed tests.
- `pytest -rx` shows the captured output of failed tests (default behaviour).
- `pytest -rA` shows the captured output of all tests.
- The formatting of the output is prettier with `-r` than with `-s`.
- `pytest -m sanity` runs only tests marked as `sanity`
- `pytest --markers` shows all the built-in markers that come with pytest and any custom ones we created and put in `pytest.ini`

## Run Test Code
- From within Visual Studio Code Terminal:
- `poetry run pytest -v` runs all tests in verbose mode
- `poetry run pytest tests/test_basics.py` runs all tests in one file
- `poetry run pytest tests/test_basics.py::test_bool` runs one test case
- `poetry run pytest -rA tests/test_pytest_examples.py --browser firefox` runs with our custom command line option

## Resources
- Head Frist Python 2nd Edition