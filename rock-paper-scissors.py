from random import randrange 
number = randrange(3) 
#print(number)

pc_choise = number
user_choise = input('rock, paper, or scissors? Or you can type End to end the game. ')

while user_choise != 'End':
    if user_choise == 'rock':
        if pc_choise == 0:
            print('The computer also chose rock. Draw.')
            break
        elif pc_choise == 1:
            print ('The computer chose scissors! Rock crushes scissors! You win!')
            break
        else:
            print ('The computer choose paper. Paper sufficates rock. Computer won!')
            break
    elif user_choise == 'scissors':
        if pc_choise == 0:
            print('The computer chose rock. Rock crushes scissors! Computer won!')
            break
        elif pc_choise == 1:
            print('The computer also chose scissors. Draw.')
            break
        else:
            print('The computer chose paper. Scissors cut paper! You win!')
            break
    elif user_choise == 'paper':
        if pc_choise == 0:
            print('The computer chose rock. Paper sufficates rock. You win!')
            break
        elif pc_choise == 1:
            print('The computer chose scissors. Scissors cut paper! Computer won!')
            break
        else: 
            print('The computer also chose paper. Draw.')
            break
    elif user_choise == 'End':
        break
    else:
        print('I do not understand.')