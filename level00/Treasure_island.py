print(r'''
***************************************************
                      /,   ,|   ,|
             /| /(  ,' / ,//
          \`( |/ /,'  (,/ |
           \ \ ` `   `  /--,
         _,_\ `  ` `  ``  /__
          '-.____________`  /
            [  \@,    :] `--,-..-
            [__________]__,'-._/
             )'o\ ' o) \/ )
             \  /   __  ./
              \=`   ==,\..
               \ -. `,' (333
               3`--''    \33.
             ,333_) /mm33333:.
            |:#:mmmmmm333333::
            |:#:333333333::##'
            ':#:ctr3333''#####\
             |:#:#\###########\
             |:#:##\###########\
             |:#:###\########|#\
             /:#:|:::\|::::::|:(
             ):#:|::::\::::::|:/
            /:#;/:::::<::::::|(
*************************************************
      
''')

print('Welcome to Treasure Island! You mission is to find the treasure :) ')
direction = input('Choose what do you  want Left or Right? ').lower()

if (direction == 'right'):
    print("Fall into a hole Game Over :/ ")
elif(direction == "left"):
    option1 = input('Swim or Wait? ').lower()
    if(option1 == 'Wait'):
        door = input("Which door? Red, Blue or Yellow? ")
        if (door == 'red'):
            print("Burned by fire , Game Over :/ ")
        elif(door == 'blue'):
            print("Eaten by the Beast, Game Over :/ ")
        elif(door == 'yellow'):
            print("You Win!")
        else:
            print("Game over :/")
    else: 
        print("Attecked by trout. Game Over!")
else:
     print("Fall into a hole Game Over :/ ")