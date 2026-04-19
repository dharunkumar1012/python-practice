# lambda argument : expression
'''
add = lambda a,b : a+b
print(add(5,5 ))
'''
'''
square = lambda x : x*x
print(square(5))
'''

# map
'''
fruits = ['apple', 'banana', 'guava']
result = list(map(lambda fruit : fruit.upper(), fruits))
print(result)
'''

# filter
'''
nums = [2, 4, 6, 89, 9, 3]
result = list(filter(lambda num: num % 2 == 0, nums))
print(result)
'''
# reduce

''' 
# reduce gives one number in the output, not a list
num = [1,2,3,5,6,7]
result = reduce(lambda a,b : a+b, num ) 
print(result)
'''
# Find max
'''
prices = [2,6,4,88,11,77,3,99]
result = reduce(lambda a,b : a if a > b else b, prices)
print(result)
'''
# Real-timd example
'''
from functools import reduce
prices = [500,600,1500,1600,900]
expensive = list(filter(lambda x : x > 1000, prices))

print(max(expensive))
'''

# closure function
'''
def outer(msg):
    def inner():
        return f"Message is {msg}"
    return inner


result = outer("Irunga Bhaii....")
print(result())
'''

# Call back function
'''A call back function that you pass as an argument to another function,
So that it can be called (executed) later, usually after some action is completed'''

'''
def on_clicked_button(callback):
    print("Button clicked")
    callback()

def show_msg():
    print("Hello Dk, Welcome!")
    
on_clicked_button(show_msg)
'''