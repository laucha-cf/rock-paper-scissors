import random
from aux_functions import who_wins

def result():
    user = input('R for rock - P for paper - S for scissors >> ').lower()
    computer = random.choice( ['r', 'p', 's'] )

    print(f'Your choice:{user} - Computer´s choice:{computer}')

    #if player and opponent are the same, then it is a tie
    if user != computer:
        if who_wins( user, computer ):
            return 'You won!'
        return 'You lost!'
    else:
        return 'It is a tie!'

    
if __name__ == '__main__':
    wanna_play = True
    while wanna_play == True:
        print(result())
        r = input('Wanna keep playing?(y/n) >> ').lower()
        if r == 'n':
            wanna_play = False
