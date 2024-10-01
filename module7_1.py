from pprint import pprint

name = 'products.txt'
file = open(name, 'a')

class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop(Product):
    def __init__(self, name: str, weight: float, category: str):
        super().__init__(name, weight, category)
        self.name = name
        self.weight = weight
        self.category = category
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = []
        products = file.read()
        file.close()
        print(f'{products}')

    def add(self, *products):
        for i in products:
            ad = (str(i))
            file = open(self.__file_name, 'r')
            f = file.read()
            file.close()
            if ad in f:
                print(f'Продукт {ad} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{ad}\n')
                file.close()

s1 = Shop('', 0, '')
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())


