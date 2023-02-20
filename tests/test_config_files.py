import configparser
import json
import openpyxl
import tomli
import yaml


def test_read_json_file():
    file_path = "config/my_config.json"
    with open(file_path, "r") as f:
        my_config = json.load(f)
    assert my_config["name"]["first-name"] == "Fred"
    assert my_config["person-info"]["age"] == 44
    assert my_config["person-info"]["employed"]
    assert my_config["person-info"]["pets"] == None

def test_read_yaml_file():
    file_path = "config/my_config.yaml"
    with open(file_path, "r") as f:
        my_config =  yaml.safe_load(f)
    assert my_config["name"]["first-name"] == "Fred"
    assert my_config["person-info"]["age"] == 44
    assert my_config["person-info"]["employed"]
    assert my_config["person-info"]["pets"] == None

def test_read_ini_file():
    file_path = "config/my_config.ini"
    my_config = configparser.RawConfigParser()
    my_config.read(file_path)
    assert my_config.get("name", "first-name") == "Fred"
    assert int(my_config.get("person-info", "age")) == 44 # Everything in .ini file is a string, have to cast
    assert bool(my_config.get("person-info", "employed")) # Here we have to cast to a bool
    
    # Not sure if .ini files can handle null/None values
    # assert config.get("person-info", "pets")

def test_read_toml_file():
    file_path = "config/my_config.toml"
    with open(file_path, mode="rb") as f:
        my_config = tomli.load(f)
    assert my_config["name"]["first-name"] == "Fred"
    assert my_config["person-info"]["age"] == 44
    assert my_config["person-info"]["employed"]

    # Not sure if .toml files can handle null/None values
    # assert my_config["person-info"]["pets"] == None

def test_read_excel_file():
    file_path = "config/my_config.xlsx"
    book = openpyxl.load_workbook(file_path)
    sheet = book.active # Get active sheet
    assert sheet.cell(row=1, column=2).value == "Fred"
    
