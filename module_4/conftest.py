import pytest

@pytest.fixture (scope="module")
def input_data():
    print("Создали список")
    return [1, 2, 3, 4, 5]