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

password = ""

total = user_digits + user_letters + user_symbols


for i in range(0, total ):
        
    if(user_letters != 0):
        user_letters -= 1
        new_list.append(random.choice(letters))
        
    if(user_symbols != 0):
        user_symbols -= 1
        new_list.append(random.choice(symbols))
    if(user_digits != 0):
        user_digits -= 1
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