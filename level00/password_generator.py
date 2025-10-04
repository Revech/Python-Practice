import random
letters = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

symbols = ['!', '@', '#', '$', '%', '&', '*']

digits = ['0','1','2','3','4','5','6','7','8','9']

print("Welcome to the PyPassword Generator")

user_letters = int(input("How many letts would you like your password to be? "))
user_symbols = int(input("how many symbols would you like? "))
user_digits= int(input("how many numbers would you like? "))

new_list = []



x =0 
for i in letters:
    x += 1
    if (x <= user_letters):
        new_list.append(random.choice(letters))
x= 0
for i in symbols:
    x += 1
    if (x <= user_symbols):
        new_list.append(random.choice(symbols))
x = 0
for i in digits:
    x += 1
    if (x <= user_digits):
        new_list.append(random.choice(digits))

for word in new_list:
    print(word, end="")


#########################
"""
What is learned:

1- to print a list with no spaces on the same line use end=""
2- adding in a list without .append will overwrite all the list values
3- changing the value inside a loop will affect the value autside of the loop as well 

"""