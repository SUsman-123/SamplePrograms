#Inheritance Problem 1
class Product:
    def __init__(self,name,price,deal_price,ratings):
        self.name=name
        self.price=price
        self.deal_price=deal_price
        self.ratings=ratings
    def display_product_Details(self):
        print("Product:{}".format(self.name))
        print("Price:{}".format(self.price))
        print("deal price:{}".format(self.deal_price))
        print("You saved:{}".format(self.price-self.deal_price))
        print("Rating:{}".format(self.ratings))
    def get_deal_price(self):
        return self.deal_price
class Electronicsitem(Product):
    def __init__(self,name,price,deal_price,ratings,warrenty_in_months):
        Product.__init__(self,name,price,deal_price,ratings)
        self.warrenty_in_months=warrenty_in_months
    def get_warrenty(self):
        return self.warrenty_in_months
class Grocery_item(Product):
    def __init__(self,name,price,deal_price,ratings,expairy_date,package_date):
        Product.__init__(self,name,price,deal_price,ratings)
        self.expairy_date=expairy_date
        self.package_date=package_date
    def display_product_Details(self):
        super().display_product_Details()
        print("Expiry Date:{}".format(self.expairy_date))
productObj=Product("Milk",100,80,5)
productObj.display_product_Details()
print("===================================")
electronicObj=Electronicsitem("Hp",5000,500,5,2)
print(electronicObj.get_warrenty())
print("=======================================")
GroceryObj=Grocery_item("Laptop",5000,50000,4,2019,2022)
GroceryObj.display_product_Details()