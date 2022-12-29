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

#Inheritance problem 2
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

class Order:
    def __init__(self,delivery_speed,delivery_address):
        self.items_in_cart=[]
        self.delivery_speed=delivery_speed
        self.delivery_address=delivery_address
    def add_item(self,product,quantity):
        self.items_in_cart.append((product,quantity))
    def display_total_bill(self):
        total_bill=0
        for product,quantity in self.items_in_cart:
            price=product.get_deal_price()*quantity
            total_bill+=price
        print("Total Bill:{}".format(total_bill))
milk=Grocery_item("Milk",40,25,4.5,2022,2019)
tv=Electronicsitem("TV",45000,40000,4,12)
order=Order("Prime Delivery","Kurnool")
order.add_item(milk,2)
order.add_item(tv,1)
order.display_total_bill()

#Inheritance problem 3
class Abc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print( self.a+self.b)
    def sub(self):
        print(self.a-self.b)
class Def(Abc):
    def __init__(self,a,b):
        Abc.__init__(self,a,b)
    def mul(self):
        print(self.a*self.b)
    def div(self):
        #return  a/b
        pass
obj1=Abc(10,20)
obj1.add()
Obj2=Def(10,20)
Obj2.mul()

#Inheritance problem 4
class HigherParentClass:
    def print_something(self):
        print("this is from higher parent class")
class LowerparentClass(HigherParentClass):
    def print_something(self):
        print("This is from lower parent class")
class ChildClass(LowerparentClass):
    def print_something(self):
        HigherParentClass.print_something(self)
childClassObj=ChildClass()
lowerClassObj=LowerparentClass()
childClassObj.print_something()
lowerClassObj.print_something()



