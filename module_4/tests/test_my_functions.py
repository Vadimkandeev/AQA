# def add(a, b):
#     return a + b
#
#
#
# class TestMyFunctions:
#     def test_positive_test_numbers(self):
#         assert add(2, 3) == 5
#
#     def test_negative_test_numbers(self):
#         assert add(-1, -4) == -5
#
#     def test_negative_and_positive_test_numbers(self):
#         assert add(5, -2) == 3
#
#     def test_add_string(self):
#         assert add("test", "string") == "test string"
import pytest
@pytest.fixture (scope="module")
def input_data():
    print("Создали список")
    return [1, 2, 3, 4, 5]

def test_sum(input_data):
    assert sum(input_data) == 15

def test_len(input_data):
    assert len(input_data) == 5