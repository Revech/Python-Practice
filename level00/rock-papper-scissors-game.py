import random

choice = int(input("Choose 1 for rock, 2 for scissors, 3 for paper: "))

random = random.randint(1,3)

if(choice >= 1 and choice <=3):
    print("You Chose: ")
    if(choice == 1):
        print("""
     _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """)

    elif(choice == 2):
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """)
        
    elif(choice == 3):
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    """)
        



    print("Computer Chose: ")

    if(random == 1):
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """)

    elif(random == 2):
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """)
        
    else:
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    """)
        
    if(random ==1 and choice == 2):
        print("You Lose!")
    elif(random == choice):
        print("It's a Tie!")
    elif(random == 2 and choice == 3):
        print("You Lose!")
    elif(random == 3 and choice == 1):
        print("You Lose!")
    else:
        print("You Win!")

else:
    print("Not Valid")