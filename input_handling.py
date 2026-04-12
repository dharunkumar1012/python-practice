#Input Handling(sys.argv)
import sys

full_name = sys.argv[1]

email = full_name.lower().replace(' ', '.')+ '@gmail.com'

print('\n--- your Profile ---')
print('Full name:', full_name)
print('Generated email:', email)
