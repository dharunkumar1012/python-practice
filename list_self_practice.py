playlist = ['Pookal pookum tharunam', 'Kanave kanave', 'kannadi poove']
favourite_foods = ['Biriyani', 'Dosa', 'Prawn Fry']
recent_locations = ['siruseri', 'kelambakkam', 'navalur']

# print(favourite_foods)

'''
for i in playlist:
    print(i)

    
for song in playlist:
    print(song + ' by DK')
'''

# Check
'''
if 'Dosa' in favourite_foods:
    print('Yes')
else: 
    print('no')
'''

# Mutable
'''
favourite_foods[1] = 'BBQ Shawarma'
print(favourite_foods)
'''

# Retrns Index value
'''
for i, location in enumerate(recent_locations):
    print(f"Location {i+1} : {location}")
'''