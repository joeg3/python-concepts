import json
import pytest


@pytest.fixture(scope='session')
def config(request):

    with open(r"config.json") as config_file:
        config = json.load(config_file)

    return config

@pytest.fixture(scope='function')
def open_close_file_path(request):
    file_name = request.param # We get file name from tests that use this fixture
    file = open(file_name)
    yield file
    file.close()

@pytest.fixture(scope='function')
def read_file_name():
    return 'text_files/read_from_file.txt'

@pytest.fixture(scope='function')
def write_file_name():
    return 'text_files/write_to_file.txt'

@pytest.fixture(scope='function')
def json_file_name():
    return 'text_files/json_file.json'