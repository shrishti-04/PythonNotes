# class Repository:
#     def __init__(self):
#         self.packages = {}
#     def get_package(self, package):
#         self.packages[package.name] = package
#     def total_size(self):
#         result = 0
#         for package in self.packages.values():
#             result += package.total_size()
#         return print(result)
    
class Clothing:
    stock = {'name': [], 'material': [], 'amount': []}
    def __init__(self, name):
        material = ''
        self.name = name
    def add_item(self, name, material, amount):
        Clothing.stock['name'].append(self.name)
        Clothing.stock['material'].append(self.material)
        Clothing.stock['amount'].append(amount)
    def stock_by_item(self, material):
        count = 0
        n = 0
        for item in Clothing.stock['material']:
            if item == material:
                count += Clothing.stock['amount'][n]
                n+=1
        return count
    
class Shirt(Clothing):
    material = 'Cotton'
class Pants(Clothing):
    material = 'Cotton'
    
polo = Shirt('Polo')
sweatpants = Pants('Sweatpants')

polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)

current_stock = polo.stock_by_item('Cotton')
print(current_stock)

# OUTPUT:
# 10