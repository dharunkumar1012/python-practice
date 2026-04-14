
from abc import ABC, abstractmethod
#There is no use of creating object for abstractmethod class:
class Parent(ABC):
    @abstractmethod
    def login(self):
        print("Lala")
        
    @abstractmethod
    def logout(self):
        print('Lippa')
        
class Child(Parent):
    def login(self):
        print("Login success.") #Over Ride
        
    def logout(self):
        print("Logout unsuccess!") #Over Ride
        
r = Child()
r.login()
r.logout()
