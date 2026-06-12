import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.database import Database
from data import *

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def database():
    return Database()

@pytest.fixture
def mock_bun():
    """Создание мок-булочки с базовыми данными."""
    mock = Mock()
    mock.get_name.return_value = TEST_BUN["name"]
    mock.get_price.return_value = TEST_BUN["price"]
    return mock

def _create_mock_ingredient(type, name, price):
    """Вспомогательная функция для создания мок-ингредиента."""
    mock = Mock()
    mock.get_type.return_value = type
    mock.get_name.return_value = name
    mock.get_price.return_value = price
    return mock

@pytest.fixture
def mock_sauce():
    """Мок соуса."""
    return _create_mock_ingredient(**TEST_SAUCE)

@pytest.fixture
def mock_filling():
    """Мок начинки."""
    return _create_mock_ingredient(**TEST_FILLING_1)

@pytest.fixture
def mock_ingredients(mock_sauce, mock_filling):
    """Список базовых ингредиентов."""
    return [mock_sauce, mock_filling]

@pytest.fixture
def burger_with_bun(burger, mock_bun):
    """Бургер с установленной булочкой."""
    burger.set_buns(mock_bun)
    return burger

@pytest.fixture
def full_burger(burger_with_bun, mock_ingredients):
    """Полностью собранный бургер (булочка + ингредиенты)."""
    for ingredient in mock_ingredients:
        burger_with_bun.add_ingredient(ingredient)
    return burger_with_bun

