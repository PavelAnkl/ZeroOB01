# Создай класс `Store`.
# Атрибуты класса: `name`: название магазина, `address`: адрес магазина, `items`: словарь, где ключ - название товара, а значение - его цена.
# Например, `{'apples': 0.5, 'bananas': 0.75}`.
# `__init__ - конструктор, который инициализирует название и адрес, а также пустой словарь для `items`
class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    # метод для добавления товара в ассортимент
    def add_item (self, item_name, price):
        self.items[item_name] = price
        print(f'Товар {item_name} был добавлен в магазин {self.name}')

    # метод для удаления товара из ассортимента
    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f'Товар {item_name} удален из магазина {self.name}')

    # метод для получения цены товара по его названию. Если товар отсутствует, возвращайте `None`
    def get_price(self, item_name):
        return self.items.get(item_name)

    # метод для обновления цены товара
    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f'Цена на товар {item_name} обновлена в магазине {self.name}')
        else:
            print(f'Товар {item_name} не найден')


# Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров
store1 = Store('Пятерочка', 'Ленина, 15')
store2 = Store('Магнит', 'Ленина, 45')
store3 = Store('Ярче', 'Ленина, 80')

store1.add_item('Хлеб', '25,50')
store1.add_item('Молоко', '42,20')
store1.add_item('Гречка', '37,10')

store1.remove_item('Хлеб')

print(store1.get_price('Молоко'))

store1.update_price('Гречка', '35,20')

print(store1.get_price('Гречка'))








