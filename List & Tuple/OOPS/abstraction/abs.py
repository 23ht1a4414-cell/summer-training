'''
what is abstraction?
Hiding the internal implimentation details
showing the essential
features to the user
         or
    what operatins will done
    But not:
    how operatiopn is working internal
-->complexity is hidden from the user

why use abstraction?
1.Reduces the complexity
2.Improves the security
3.Better maintaince
4.Cleaner code
5.Standardization


#Abstraction in python
python supports abs using
abstract classes
abstract methods

#ABC module
ABC --abstract base class


Abstract class
Blue print of a class
can't create objects directly

# defines basic common structure

abstract can have:
1.abs methods
2.normal methods

#Abs method
methods declared but:
 implimentation not proved

 child class must Impliment it
Examle:
vehicle

->start()

'''

#ABC --> Abstract base class
from abc import ABC,abstractmethod
#abstract class
class vehicle(ABC):
   #abstract method
   @abstractmethod
   def start(self):
        pass
class car(vehicle):
    def start(self):
        print("car started")
c1 = car()
c1.start()

#Example.2
from abc import ABC,abstractmethod
class animal(ABC):
       @abstractmethod
       def sound(self):
           pass
class dog(animal):
     def sound(self):
          print("dog barks")
d1 =dog()
d1.sound()

#multiple abstractmethod
class shape(ABC):
      @abstractmethod
      def area(self):
           pass
      @abstractmethod
      def perimeter(self):
           pass
class rectangle(shape):
     def area(self):
          print("area formula")
     def perimeter(self):
          print("perimeter formula")
r1 = rectangle()
r1.area()

#Example.3
#payment system
#pay()
class paymentGateway(ABC):
      @abstractmethod
      def pay(self):
           pass
class phonepe(paymentGateway):
     def pay(self):
      print("paid using phonepe")
class paytm(paymentGateway):
     def pay(self):
      print("paid using paytm")
pp =phonepe()
pt =paytm()
pp.pay()
pt.pay()

#task:create a abstract class payGateway
'''with 2 abs method
1.pay
2.refund
but amount --:param
create child class implimentations
1.creditcardpay
2.UPI pay
'''
from abc import ABC, abstractmethod
class PayGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    @abstractmethod
    def refund(self, amount):
        pass
class CreditCardPay(PayGateway):
    def pay(self, amount):
        print("Credit Card Payment:", amount)

    def refund(self, amount):
        print("Credit Card Refund:", amount)
class UPIPay(PayGateway):
    def pay(self, amount):
        print("UPI Payment:", amount)
    def refund(self, amount):
        print("UPI Refund:", amount)

c = CreditCardPay()
c.pay(1000)
c.refund(500)

u = UPIPay()
u.pay(2000)
u.refund(1000)

'''
create an abstract class Employee
with abs methods:
calculate_salary()
create:
FulltimeEmployee
parttimeEmployee
Rules:fulltime salary = 50000
parttime salary = hours*500

'''
from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 50000


class PartTimeEmployee(Employee):
    def __init__(self, hours):
        self.hours = hours

    def calculate_salary(self):
        return self.hours * 500
full_time_emp = FullTimeEmployee()
print("Full-time Employee Salary:", full_time_emp.calculate_salary())
part_time_emp = PartTimeEmployee(40)
print("Part-time Employee Salary:", part_time_emp.calculate_salary())

'''
create an abs class restaurant with methods:
prepare_food()
delivery_time()
create child classes:
1.pizzashop
2.burger shop
display:
food preparation message

'''
from abc import ABC, abstractmethod
class Restaurant(ABC):
    @abstractmethod
    def prepare_food(self):
        pass

    @abstractmethod
    def delivery_time(self):
        pass
class PizzaShop(Restaurant):
    def prepare_food(self):
        print("Preparing delicious pizza...")

    def delivery_time(self):
        print("Pizza will be delivered in 30 minutes.")
class BurgerShop(Restaurant):
    def prepare_food(self):
        print("Preparing tasty burger...")

    def delivery_time(self):
        print("Burger will be delivered in 20 minutes.")
pizza_shop = PizzaShop()
pizza_shop.prepare_food()
pizza_shop.delivery_time()
burger_shop = BurgerShop()
burger_shop.prepare_food()
burger_shop.delivery_time()
'''
ride booking application
class->Ride
calculate_fare(distance)
child :
1.bikeride
2.carride
3.auto ride

rules:
bikeride ---> = distance*10
carride --> = distance*20
autoride --> = distance*15
'''
from abc import ABC, abstractmethod
class Ride(ABC):c
    @abstractmethod
    def calculate_fare(self, distance):
        pass
class BikeRide(Ride):
    def calculate_fare(self, distance):
        return distance * 10

class CarRide(Ride):
    def calculate_fare(self, distance):
        return distance * 20

class AutoRide(Ride):
    def calculate_fare(self, distance):
        return distance * 15
bike_ride = BikeRide()
car_ride = CarRide()
auto_ride = AutoRide()
distance = 10
print("Bike Ride Fare:", bike_ride.calculate_fare(distance))
print("Car Ride Fare:", car_ride.calculate_fare(distance))
print("Auto Ride Fare:", auto_ride.calculate_fare(distance))
