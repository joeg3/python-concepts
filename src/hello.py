import sys


def print_version():
    print("Hello")
    print('Python Version (sys.version)', sys.version)
    print(sys.version)
    version = str(sys.version_info.major) + '.' + str(sys.version_info.minor) + '.' + str(sys.version_info.micro) + '.' + str(sys.version_info.releaselevel)
    print("**************Python version: (sys.version_info.major) etc.", version)