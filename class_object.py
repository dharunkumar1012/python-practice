# Class and Object
'''
class Student:
    def say_hello(self):
        print('Hi, students!')


v = Student() #object Creation
v.say_hello()
'''
# Constructor
'''
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
result = Student('Dharun', 22)
result.display()
'''

'''
class Employee:
    def __init__(self, name, aadhaar):
        self.name = name
        self.aadhaar = aadhaar

    def enter_office(self):
        print(f"{self.name} enter using aadhaar {self.aadhaar}")

    def open_bank_account(self):
        print(
            f"Bank account opened for {self.name} with aadhaar {self.aadhaar} ")

result = Employee('DK', '7777 8888 9999')
result.enter_office()
result.open_bank_account()
'''