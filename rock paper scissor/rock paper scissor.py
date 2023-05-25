import random
print('Wining rule of the game rock paper scissor are :\n ' + "Rock VS paper -> paper Win \n"
      +"Rock VS Scissor -> Rock Win \n"
      +"paper VS Scissor -> Scissor \n")
while True:
    print("Enter your choice \n 1- Rock \n 2- paper \n 3- Scissor\n")

    choice = int(input("Enter your choice:"))

    while choice > 3 or choice <1:
        choice=int(input("Enter a valid choice please"))
        if choice ==1:
            choice_name ='rock'
        elif choice ==2:
            choice_name='paper'
        else:
            choice_name='scissors'

        print('user choice is \n', choice_name)
        print('now its computer turn ....')

        comp_choice = random.randint(1,3)

        while comp_choice==choice:
            comp_choice= random.randint(1,3)
        if comp_choice ==1:
            comp_choice_name = 'Rock'
        elif comp_choice ==2:
            comp_choice_name= 'Paper'
        else:
            comp_choice_name ='Scissore'
        print ("computer choice is comp_choice_name")
        print(choice_name,"vs",comp_choice_name)

        if choice ==comp_choice:
            print('its a draw',end ='')
            result="DRAW"
        if(choice == 1 and comp_choice==2 ):
            print('paper win =>',end="")
            result='paper'
        elif (choice == 2 and comp_choice == 1):
            print ('paper Win= =>',end="")
            result="paper"

        if (choice == 1 and comp_choice == 3):
            print ('rock win => end=')
            result="rock"
            #elif (choice==3 and comp_choice==1):
            print ('rock win => end==')
            Result="rock"

        if (choice==2 and comp_choice==1):
            print('scissor Win => end=')
            result='scissor'
        elif (choice == 3 and comp_choice == 2):
            print('scissor win =>',end="")
            Result="rock"
        #Computer Win or Draw
            if result =='DRAW':
                print("<== its a tie ==>")
            if result ==choice_name:
                print("<== user win ==>")
            else:
                print("<== computer Win ==>")
            print("do you want to play again ?(Y/N)")
            ans=input().lower
            if ans =='n':
                break
                print ("thanks for playing")





























