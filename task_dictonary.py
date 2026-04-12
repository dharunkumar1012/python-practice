a = {}

name = input('Enter your name:')
science = int(input('science mark:'))
social = int(input('social mark:'))
math = int(input('Math mark:'))
total = sum([science,social,math])
average = total / 3

a['Name'] = name
a['Science'] = science
a['Social'] = social
a['Math'] = math
a['Total'] = total
a['Average'] = average
print(a)
