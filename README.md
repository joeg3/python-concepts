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

## Run Test Code
- From within Visual Studio Code Terminal:
- `poetry run pytest -v` runs all tests in verbose mode
- `poetry run pytest tests/test_basics.py` runs all tests in one file
- `poetry run pytest tests/test_basics.py::test_bool` runs one test case

See my [joeg3/pytest-concepts](https://github.com/joeg3/pytest-concepts) repo for example of the many command line options for pytest.
