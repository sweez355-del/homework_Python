import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("тест", "Тест"), ("04 апреля 2023", "04 апреля 2023"), ("123", "123")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""), ("Skypro", "Skypro"),
    ("Hello world", "Hello world"),
    ("Skypro ", "Skypro "), (" Hello World ", "Hello World ")
])
def test_trim_negative(input_str, expected):
    utils = StringUtils()
    assert utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" Skypro", "Skypro"),
    (" Hello World", "Hello World"), ("  ", "")
])
def test_trim_positive(input_str, expected):
    utils = StringUtils()
    assert utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, res", [
    ("SKYPRO", "s", False),
    ("skypro", "Y", False),
    ("", "s", False)
])
def test_contains_negative(string, symbol, res):
    utils = StringUtils()
    assert utils.contains(string, symbol) == res


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, res", [
    ("Skypro", "S", True),
    ("SKYPRO", "O", True),
    ("Skypro12", "12", True)
])
def test_contains_positive(string, symbol, res):
    utils = StringUtils()
    assert utils.contains(string, symbol) == res


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, res", [
    ("", "s", ""),
    ("123", "q", "123"),
    ("SKYPRO", "s", "SKYPRO")
])
def test_delete_symbol_negative(string, symbol, res):
    utils = StringUtils()
    assert utils.delete_symbol(string, symbol) == res


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, res", [
    ("123", "12", "3"),
    ("Skyro", "ro", "Sky"),
    ("Skypro Forever", "o", "Skypr Frever")
])
def test_delete_symbol_positive(string, symbol, res):
    utils = StringUtils()
    assert utils.delete_symbol(string, symbol) == res
