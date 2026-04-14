# Write
'''
file = open("notes.txt", "w")
file.write("Welcome to python file handling!\n ")
file.write("This is new file\n")
file.close()
'''

# Read
'''
file = open("notes.txt","r")
content = file.read()
print("File content:\n", content)
file.close()
'''
# Append
'''
file = open("notes.txt", "a")
file.write("Adding a new line.\n")
file.close()
'''

# with
'''
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())
'''
# User input
feedback = input("Enter your feedback:")
with open("feedback_log.txt", "a") as f:
    f.write(feedback + "\n")
print("Thanks for your feedback.")
