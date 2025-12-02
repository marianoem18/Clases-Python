import json

new_product = {
    "name": "PC-GAMER",
    "price": 1200,
    "quantity": 30,
    "brand": "TechBrand",
    "category": "Electronics",
    "entry_date": "2024-06-15"
}
with open('products.json', mode='r') as file:
    products = json.load(file)

products.append(new_product)

with open('products.json', mode='w') as file:
    json.dump(products, file, indent=4)

