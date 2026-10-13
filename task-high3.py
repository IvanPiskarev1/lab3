class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_info(self):
        print(f"{self.name} - {self.price} руб.")


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def remove_product(self, product):
        if product in self.items:
            self.items.remove(product)

    def show_cart(self):
        for product in self.items:
            product.show_info()

    def get_total(self):
        total = 0

        for product in self.items:
            total += product.price

        return total


phone = Product("iPhone", 49990)
keyboard = Product("Клавиатура", 3499)

cart = Cart()

cart.add_product(phone)
cart.add_product(keyboard)

print("Товары в корзине:")
cart.show_cart()

print(f"Общая стоимость - {cart.get_total()} руб.")