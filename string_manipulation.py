'''
name = 'dharun kumar'

print(name.lower())
print(name.upper())
print(name.capitalize())
'''

#[:2] it gives the first two numbers,[2:] it drop the first two nmbers and show the rest of the numbers
#[-2:] it gives the last two numbers, [:-2] it drop the last two nmbers and show the rest of the numbers (- means reverse)
'''
mobile = '8947563159'
masked = mobile[:2] + '******' + mobile[-2:]
print(masked)
'''
'''
song = 'mocking Bird'
artist = 'EmInEm'
formatted = f"{song.title()} - {artist.title()}"
print(formatted)
'''

'''
location = 'Padur'
location_2 = location.replace('Padur', 'Thiruporur')
print(location_2)
'''

'''
msg = 'Your uber booking id is:35649.Please keep it safe.'
booking_id = msg.split(":")[1].split(".")[0]
print(booking_id)
'''
'''
coupon_msg = 'Use Dk100 to get 100 off on your first order.'
if 'Dk100' in coupon_msg:
    print('Offer applied')
'''

'''
feedback = 'The food was so good and the owner is very humble and good guy'
print('Position is:', feedback.find('humble'))
'''

'''
name = 'dharun kumar'
initial = " ".join(word[0].upper() for word in name.split())
print(initial)
'''
'''
dirty_input = '   Lalalala     '
convert = dirty_input.strip()
print(convert)
'''

'''
word = 'Yesterday i saw one movie which was srime genre'
word1 = len(word.split())
print(word1)
'''









