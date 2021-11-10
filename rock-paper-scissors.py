from random import randrange 
number = randrange(3) 
#print(number)
while True:
    pc_choise = number
    user_choise = input('rock, paper, or scissors? Or you can type End to end the game. ')


    if user_choise == 'rock':
        if pc_choise == 0:
            print('The computer also chose rock. Draw.')
        elif pc_choise == 1:
            print ('The computer chose scissors! Rock crushes scissors! You win!')
            
        else:
            print ('The computer choose paper. Paper sufficates rock. Computer won!')
            
    elif user_choise == 'scissors':
        if pc_choise == 0:
            print('The computer chose rock. Rock crushes scissors! Computer won!')
            
        elif pc_choise == 1:
            print('The computer also chose scissors. Draw.')
            
        else:
            print('The computer chose paper. Scissors cut paper! You win!')
            
    elif user_choise == 'paper':
        if pc_choise == 0:
            print('The computer chose rock. Paper sufficates rock. You win!')
            
        elif pc_choise == 1:
            print('The computer chose scissors. Scissors cut paper! Computer won!')
            
        else: 
            print('The computer also chose paper. Draw.')
            
    elif user_choise == 'End':
        break
    else:
        print('I do not understand.')