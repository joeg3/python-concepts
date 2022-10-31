import json
import pytest

# def pytest_addoption(parser):
#     parser.addoption('--username', required=True, help='Enter email username')
#     parser.addoption('--password', required=True, help='Enter email password')

# Get config from config.json and command line
@pytest.fixture(scope='session')
def config(request):

    with open(r"config.json") as config_file:
        config = json.load(config_file)

    #config['username'] = request.config.getoption('--username')
    #config['password'] = request.config.getoption('--password')
    return config