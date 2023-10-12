# Import the libraries
import random
from string import punctuation

# Initialize the variables
password = " "
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"

# User's Choice to select the type of password
print("~~~RANDOM PASSWORD GENERATOR~~~")
print("1.Password without Special Characters")
print("2.Password with Special Characters")

choice = int(input("Enter your Choice = "))

# Get the password length
length = int(input("\nEnter the length of the string = "))

# Logic: Password without Special Characters
if choice == 1:
    char_choice = input("\nDo you wish to add the lowercase characters in your password (yes / no / both) = ")
    for i in range(length):

        # Logic: Include lower case and numbers
        if char_choice.lower() == 'yes':
            init_pwd = lower + numbers
            password = "".join(random.sample(init_pwd, length))

        # Logic: Include upper case and numbers
        elif char_choice.lower() == 'no':
            init_pwd = upper + numbers
            password = "".join(random.sample(init_pwd, length))

        # Logic: Include upper case, lower case and numbers
        elif char_choice.lower() == 'both':
            init_pwd = upper + lower + numbers
            password = "".join(random.sample(init_pwd, length))
        else:
            print("Type correct option")
    print(f"\nRandom Generated password is   {password}")

# Logic: Password with Special Characters
elif choice == 2:
    char_choice = input("\nDo you wish to add the lowercase characters in your password (yes/no/both) = ")
    for i in range(length):

        # Logic: Include lower case and numbers
        if char_choice.lower() == 'yes':
            init_pwd = lower + numbers + punctuation
            password = "".join(random.sample(init_pwd, length))

        # Logic: Include upper case and numbers
        elif char_choice.lower() == 'no':
            init_pwd = upper + numbers + punctuation
            password = "".join(random.sample(init_pwd, length))

        # Logic: Include upper case, lower case and numbers
        elif char_choice.lower() == 'both':
            init_pwd = upper + lower + numbers + punctuation
            password = "".join(random.sample(init_pwd, length))
        else:
            print("Type correct option")
    print(f"\nRandom Generated password is  {password}")

# Logic: Invalid Case
else:
    print("\nPlease provide the correct option (1 / 2)!")