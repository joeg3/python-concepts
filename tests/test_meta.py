import sys

from importlib.metadata import version


def test_get_python_version():
    version = str(sys.version_info.major) + '.' + str(sys.version_info.minor) + '.' + str(sys.version_info.micro) + '.' + str(sys.version_info.releaselevel)
    print("**************Python version: ", version)
    assert sys.version_info.minor == 10

def test_get_version_of_package():
    v = version('pytest')
    print("**************Pytest version: ", v)