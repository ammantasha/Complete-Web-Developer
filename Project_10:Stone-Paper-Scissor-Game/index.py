from random import *

print("Rules : \n 1. Stone VS Paper = Paper Wins \n 2. Stone VS Scissor = Stone Wins \n 3. Paper VS Scissor = Scissor Wins \n NOTE : If you want to quit the game , Press Ctrl+C...")
print("\n Options :- \n 1. Stone\n 2. Paper \n 3. Scissor \n ")

while True:
    try:      
        user_input = int(input("Enter your choice : "))

        if user_input < 4 and user_input >0:
            if user_input == 1:
                user = 'Stone'
            elif user_input == 2:
                user = 'Paper'
            else:
                user = 'Scissor'
            print('\nWait !!! Computer is selecting the input')
            
            comp_input = randint(1,3)
            if comp_input == 1:
                comp = 'Stone'
            elif comp_input == 2:
                comp = 'Paper'
            else:
                comp = 'Scissor'
            print(comp,end='\n')
            
            if user == comp:
                print('\n--------------Tie--------------\n')
            else:
                if (comp == 'Stone' and user == 'Paper') or (comp == 'Paper' and user == 'Scissor') or (comp == 'Scissor' and user == 'Stone'):
                    print('\n--------------User Wins--------------\n')
                elif (user == 'Stone' and comp == 'Paper') or (user == 'Paper' and comp == 'Scissor') or (user == 'Scissor' and comp == 'Stone'):
                    print('\n--------------Computer Wins--------------\n')
        else:
            print('Bad Choice\n')

    except KeyboardInterrupt:
        print('Thanks for playing')
        break
