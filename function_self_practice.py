# Function (function without  argument and without return)
'''
def greet():
     print('Welcome to function')
greet()
'''
# Function With argument: (Function With one argument and without return)
'''
def great(name):
    print(f'Hello {name} Welcome.')
great('Dharun')
'''

# Function with 2 arguments:
'''
def fun(a,b): 
    print(a+b)
fun(5,5)
'''

# Function with argument and with return
'''
def func(a: int,b: int):
    return a+b

result = func(5,5)

print(result)
'''

# Function with *args
'''
def fun(*args):
    total = 0
    for num in args:
        total += num
    return total

print(fun(1,2,5,6,7))
'''
# Function with kargs
'''
def fun(**kargs):
    print('User profile: ')
    for key,value in kargs.items():
        print(f'{key}: {value}')

fun(name='Dharun', age='22', job='VIP')
'''
