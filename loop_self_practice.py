#if statement
'''
order_amount = 1000
day = 'mon'
membership = 'gold'

if (order_amount >= 1000 and day in ['sat', 'sun']) or membership == 'gold':
    print('20% discount!')
else:
    print('No Offer.')
'''

#For loop
'''
names = ['dharun', 'kumar', 'raj', 'gopal', 'baba']
for i in names:
    print(i.upper())
'''

#While loop
'''
correct_pin = '6381'
enter_pin = ''

while enter_pin != correct_pin:
    enter_pin = input('Enter a pin:')
print('Access Granted.')
'''

'''
for i in range(1,11):
    if i == 5:
        break
    print(i)
'''
'''
a=[1,2,3,4,8,9,7,5,69,87,93]
for i in a:
    if i == 5:
        break
    print(i)
'''

'''
count = 5
while count > 0:
    print(f'countdown: {count}')
    count -= 1
print("Times's up")
'''

'''
items = []

while True:
    item = input("Add item(type 'done' to finish):")
    if item.lower() == 'done':
        break
    items.append(item)
print('Items in cart', items)
'''








