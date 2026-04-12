#1.
'''
print(5 + 2 * 3)
'''

#2.
'''
x = 5
y = 2
print(x > y and x != y or y == 2)
'''

#3.
'''
a = 5
b = 2
c = a**b
print(c)
'''

#6.
'''
num = int(input('Enter a value:'))
if num %4 == 0 and num %8 != 0:
    print('Condition is satisfied.')
else:
    print('Condition is not satisfied.')
'''

#7.
'''
year = int(input('Enter a year:'))
if (year %4 == 0 and year %100 != 0) or (year %400 == 0):
    print('It is leap year.')
else:
    print('It is not a leap year.')
'''

#8
'''
num = int(input('Enter a value:'))

if num < 10:
    print('Small')
elif num <= 50:
    print('Medium')
else:
    print('Large')
'''

#9
'''
a = 1
total = 0
while a <= 50:
    total = total + a
    a += 1
print("Total:", total)
'''

#10.
'''
for i in range(1, 11):
    print('7 x', i, '=', i*7)
'''

#11.
'''
for i in range(1, 51):
    if i %5 == 0:
        print(i)
'''

#12.
'''
num = int(input('Enter a value:'))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
    print('Factorail:', factorial)
'''

#13.
'''
for i in range(1,5):
    for j in range(1, i+1):
        print(i, end = ' ')
    print()
'''

#14.
#Increment
'''
for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end = ' ')
    print()

#Decrement
for i in range(3, 0, -1):
    for j in range(1, i+1):
        print(j, end = ' ')
    print()
'''

#15.
#Break
'''
for i in range(1,21):
    if i == 10:
        break
    print(i)
'''
#continue
'''
for i in range(1, 21):
    if i == 10:
        continue
    print(i)
'''
#pass
'''
for i in range(1, 21):
    if i == 10:
        pass
    print(i)
'''

