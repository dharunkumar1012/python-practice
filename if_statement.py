#Simple if
'''
age = int(input('Enter your age:'))
if age >= 18:
    print('Eligible')
'''

#if else
'''
age = int(input('Enter your age:'))
if age >= 18:
    print('Eligible')
else:
    print('Not Eligible')
'''

#if elif else
'''
age = int(input('Enter your age:'))

if age >= 18:
    print('Eligible')
elif age == 17:
    print('Apply next year.')
elif age == 16:
    print('Apply after 2 years.')
else:
    print('Not eligible.')
'''

#Nested if
'''
age = int(input('Enter your age:'))

if age >= 18:
    print('Eligible')
    
    gender = input('Enter your gender:')
    if gender == 'male' or gender == 'MALE':
        print('Given candiate is male.')

    else:
        print('Given candidate is female')
else:
    print('Not eligible.')
'''
