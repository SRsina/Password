#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
a = len(letters)
b = len(numbers)
c = len(symbols)
letter_password = ""
for i in range(nr_letters):
  r = random.randint(0,a-1)
  letter_password+=(letters[r])
number_password = ""
for i in range(nr_numbers):
  r = random.randint(0,b-1)
  number_password+=(numbers[r])
symbols_password = ""
for i in range(nr_symbols):
  r = random.randint(0,c-1)
  symbols_password+=(symbols[r])
print("Your password is: " + letter_password + number_password + symbols_password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
a = len(letters)
b = len(numbers)
c = len(symbols)
password = ""
while len(password) < nr_letters + nr_numbers + nr_symbols:
  if nr_letters > 0:
    r = random.randint(0,a-1)
    password += letters[r]
    nr_letters -= 1
  if nr_numbers > 0:
    r = random.randint(0,b-1)
    password += numbers[r]
    nr_numbers -= 1
  if nr_symbols > 0:
    r = random.randint(0,c-1)
    password += symbols[r]
    nr_symbols -= 1
print("Your password is: " + password)
