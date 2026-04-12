#1.while Loop(lopp odd numbers between 50 to 78)
'''
a = 50
while a <= 78:
    if a %2 != 0:
        print(a)
    a += 1
else:
    print('Completed.')
'''
#2.Nested Loop (1234)
#(While_loop)
'''
a = 1
while a <= 4:
    b = 1
    while b <= 4:
        print(a, end = ' ')
        b += 1
    print('\n')
    a += 1
'''

#(For-loop)
'''
for i in range(1,5):
    for j in range(1,5):
        print(i, end = ' ')
    print('\n')
'''

#3.Nested Loop (****) using while
'''
a = 5
while a >= 1:
    b = 1
    while b <= a:
        print('*', end = ' ')
        b += 1
    print('\n')
    a -= 1
'''

#For Loop(lopp odd numbers between 50 to 78)
'''
for i in range(50,79):
    if i %2 != 0:
        print(i)
else:
    print('Completed.')
'''

#Nested Loop (While-loop)
'''
r = 1
while r <= 4:
    c = 1
    while c <= r:
        print(c, end = ' ')
        c += 1
    print('\n')
    r += 1
'''
#Nested Loop (For-loop)
'''
for i in range(1,5):
    for j in range(1,i+1):
        print(j, end = ' ')
    print('\n')
'''
