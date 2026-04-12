#1.Odd or Even:
'''
num = int(input('Enter a number:'))
if num %2 == 0:
    print('Even')
else:
    print('Odd')
'''

#2.Positive, Negative and zero:
'''
num = int(input('Enter a number:'))
if num > 0:
    print('Positive')
elif num < 0 :
    print('Negative')
else:
    print('Zero')
'''

#3.Greatest of two numbers:
'''
num1 = int(input('Enter a number:'))
num2 = int(input('Enter a number:'))

if num1 > num2:
    print(num1, 'is the greatest.')
elif num1 < num2:
    print(num2, 'is the greatest.')
else:
    print('invalid input')
'''

#4.Pass or Fail:
'''
std_mark = int(input('Enter your mark:'))
if std_mark >= 35:
    print('Pass')
else:
    print('Fail')
'''

#5.Grade System:
'''
mark = int(input('Enter your mark:'))
if (mark >= 90):
    print('A')
elif (mark >= 75):
    print('B')
elif (mark >= 50):
    print('c')
else:
    print('Fail')
'''
#6.Smallest of three numbers:
'''
a = int(input('Enter a value:'))
b = int(input('Enter a value:'))
c = int(input('Enter a value:'))
if (a <= b) and (a <= c):
    print(a, 'is the smallest of three number.')
elif (b <= a) and (b <= c):
    print(b, ' is the smallest of three number.')
else:
    print(c, 'is the smallest of three number.')
'''

#7.Check Character:
'''
a = input('Enter a character:')
if (a in ['a', 'e', 'i', 'o', 'u']):
    print('Vowels')
else:
    print('Consonant.')
'''

#8.Divisible by both 5 and 11:
'''
a = int(input('Enter a value:'))
if(a %5 == 0) and (a %11 == 0):
    print('It is divisible by both 5 and 11.')
else:
    print("It is not divisible by 5 and 11.")
'''
