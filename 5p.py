# password generator
import random
import string
# ask user for password length
length=int(input("Enter the length of your password:  "))
symbol=input("Wanna include symbol (yes/no) : ").lower()
characters = string.ascii_letters + string.digits
# optional
if symbol=="yes":
    characters += string.punctuation
else:
    print("\nYour password is weaker without symbols.")    
password=" "
for i in range(length):
    password+=random.choice(characters)
print("\n Password Generanted")
print(password)
score = 0

# check length
if length >= 8:
    score += 1

if length >= 12:
    score += 1

# check numbers
# char is just a temporary variable name.
# any() checks whether there is at least one True value in the iterable
if any(char.isdigit() for char in password):
    score += 1

# check uppercase
if any(char.isupper() for char in password):
    score += 1

# check symbols
if any(char in string.punctuation for char in password):
    score += 1

# final result
if score <= 2:
    print("Weak Password")

elif score <= 4:
    print("Medium Password")

else:
    print("Strong Password")
