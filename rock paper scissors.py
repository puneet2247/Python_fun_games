import random


def play():
    user = input("Choose one out of three : 'r' for rock, 'p' for paper and 's' for scissors \n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer :
        return "It's a Tie!"
    
    if is_Win(user,computer):
        return "You Won!"

    return "You lost!"

def is_Win(player,opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    # r > s, s > p, p > r
    
 
print(play())