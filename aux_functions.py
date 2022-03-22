import random

def who_wins( player, opponent ):
    #r > s - s > p - p > r
    #return true if the player wins
    if (player == 'r' and opponent == 's'):
        return True
    elif (player == 's' and opponent == 'p'):
        return True
    elif(player == 'p' and opponent == 'r'):
        return True
    else:
        return False

