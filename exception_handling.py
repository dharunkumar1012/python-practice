'''
try:
    a = int(input("Enter a number:"))
    b = int(input("Enter a number:"))
    c = a/b
    print("Value:", c)
    
except ZeroDivisionError:
    print("It is not divisible.")

except Exception:
    print("Given data is not  a number.")

finally:
    print("Completed.")
'''
'''
try:
    print("Welcome to Zomato!")
    number_of_items = int(input("How many items:"))
    total_price = 200 * number_of_items
    average_price = total_price / number_of_items
    print("Average price per item:", average_price)

except ZeroDivisionError:
    print("It is not divisible by 0.")
    
except Exception:
    print("Given data is not a number.")
    '''