# Single Inheritance:
'''
class Parent:
    def pr(self):
        a = 100
        self.a = a
        print('a:', a)
        
class Child(Parent):
    def ch(self):
        self.pr()
        b = 10
        print('b', b)
        c = self.a + b
        print('c:', c)
        
result = Child()
result.ch()
'''

#Multilevel Inheritance:
'''
class grandparent:
    def gpr(self):
        a = 100
        self.a = a 
        print('a:', a)

class parent(grandparent):
    def pr(self):
        self.gpr()
        b = 200
        self.b = b
        print("b:", b)
        
class child(parent):
    def ch(self):
        self.pr()
        c = 300
        print("c:", c)
        d = self.a + self.b + c
        print("Total:", d)
        
result = child()
result.ch()      
'''

#Multiple Inheritance:
'''
class Father:
    def fr(self):
        a = 100
        self.a = a
        print("a:", a)
        
class Mother:
    def mr(self):
        b = 200
        self.b = b
        print("b:", b)
        
class Child(Father, Mother):
    def ch(self):
        self.fr()
        self.mr()
        c = self.a + self.b
        print("c:", c)
        
Result = Child()
Result.ch()
'''
# ----------X-----------X----------
'''
class Parent:
    def pr(self):
        a = 2000
        self.a = a
        print("a:", a)
        
class Child_1(Parent):
    def ch_1(self):
        self.pr()
        b = 1000
        print("b:", b)
        c = self.a + b
        print("c:", c)
        
class Child_2(Parent):
    def ch_2(self):
        self.pr()
        d = 1500
        print("d:", d)
        e = self.a + d
        print("e:", e)
        
r = Child_1()
r.ch_1()

r1 = Child_2()
r1.ch_2()
'''

'''
class Parent:
    def pr(self):
        a = 10
        b = 5
        self.a = a
        self.b = b
        print("a:", a)
        print('b:', b)


class Child(Parent):
    def ch(self):
        super().pr()
        c = 5
        self.c = c
        print("c:", c)

    def pr(self):
        d = 100
        self.d = d
        print('d:', d)
        print("Total:", self.a + self.b + self.c + self.d)


c = Child()
c.ch()
c.pr()
'''
'''
from parent_class import Dad


class Son(Dad):
    def factory(self):
        print("colour: white")
        
    def house(self):
        print('lipa')


s = Son()
s.factory()
s.house()
'''
