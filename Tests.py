import pytest
from main import Category
from main import Product


@pytest.fixture
def category():
    return Category('яблоко', 'зеленое', 'фрукты')


def test_init(Category):
    assert Category.name == "яблоко"
    assert Category.description == "зеленое"
    assert Category.products == "фрукты"


@pytest.fixture
def product():
    return Product('яблоко', 'зеленое', '250', '1000')


def test_init1(Product):
    assert Product.name == "яблоко"
    assert Product.description == "зеленое"
    assert Product.price == "250"
    assert Product.quantity == "1000"
