#1.
a = [1,5,6,5,8,9,7,0,3,7]
'''
print(a)
print(sum(a))
'''
#2
largest = a[0]
smallest = a[0]

for i in a:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i
print('Largest:',largest)
print('Smallest:',smallest)
