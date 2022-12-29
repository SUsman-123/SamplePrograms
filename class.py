#Instance Method
class Car:
    someclassdummy="dummy"
    def sample_car_instance_method(self,a):
        print(a)
        print(self.someclassdummy)
carObj=Car()
carObj.sample_car_instance_method("Hello again!")

carObj2=Car()
carObj2.sample_car_instance_method(2)


class CarSample:
    dummyvar1="dummyvar1"
    dummyvar2="dummyvar2"
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def displayCarDetails(self):
        print(self.name)
        print(self.model)
carObj=CarSample("RD","A5")
carObj.displayCarDetails()


#Static Method
class StaticClass:
    @staticmethod
    def sample_static_method_addition(x,y):
        return x+y
    @staticmethod
    def sample_static_method_multiplication(x,y):
        return x*y
staticObj=StaticClass()
output_add=staticObj.sample_static_method_addition(2,3)
output_mul=staticObj.sample_static_method_multiplication(2,3)
print(output_add,output_mul)
StaticClass.sample_static_method_addition(2,3)

#Class Method
class ClassMethodEx:
    classVar1=False
    classVar2="ON"
    @classmethod
    def sample_class_method(cls):
        cls.classVar1=True
        cls.classVar2="OFF"
ClassMethodEx.sample_class_method()
print(ClassMethodEx.classVar1)
print(ClassMethodEx.classVar2)

class Car:
    def __int__(self,name,model):
        self.name=name
        self.model=model
    @classmethod
    def price(cls,name,year):
        return cls(name,"2022")
Car.price("Audi",2015)


#Car problem
#Car attributes: color,max_speed,accelaration, tyre_friction,start_engine,current_speed
#Car Methods:
class Car:
    def start_engine(self):
        self.is_engine_started_to=True
        print("engine is started")
    def stop_engine(self):
        self.is_engine_started_to=False
        print("Engine stoped")
    def new_car_is_created(self):
        print("New car is created")
objCar=Car()
objCar.start_engine()
objCar.stop_engine()
objCar.new_car_is_created()










