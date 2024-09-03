class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        self.reviews = []

    def sell_product(self, name, description, price):
        return Product(name, description, self, price)

    def buy_product(self, product):
        product.available = False

    def write_review(self, description, product):
        review = Review(description, self, product)
        self.reviews.append(review)
        product.reviews.append(review)
        return review

class Product:
    def __init__(self, name, description, seller, price):
        self.name = name
        self.description = description
        self.seller = seller
        self.reviews = []
        self.price = price
        self.available = True

class Review:
    def __init__(self, description, user, product):
        self.description = description
        self.user = user
        self.product = product


brianna = User(1, 'Brianna')
mary = User(2, 'Mary')

keyboard = brianna.sell_product('Keyboard', 'A nice mechanical keyboard', 100)
print(keyboard.available) 

mary.buy_product(keyboard)
print(keyboard.available)  

review = mary.write_review('This is the best keyboard ever!', keyboard)
print(review in mary.reviews)  
print(review in keyboard.reviews)  
