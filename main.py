class Category:
    name: str
    description: str
    products: list
    all_categories: list
    total_category: int
    total_unique_product: int

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        self.total_category = 0
        self.total_unique_product = 0


cat_1 = Category('яблоко', 'зеленое','фрукты')

print(cat_1.name)
print(cat_1.description)
print(cat_1.products)


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


prod_1 = Product('яблоко', 'зеленое', '250', '1000')

print(prod_1.name)
print(prod_1.description)
print(prod_1.price)
print(prod_1.quantity)