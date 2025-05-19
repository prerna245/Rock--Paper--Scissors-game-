import random 

def play():
    user = input("What's your choice:'s' for scissor, 'p' for paper, 'r' for rock :")
    computer= random.choice(['r','p','s'])

    if user == computer:
        return "Tie"
    elif who_wins(user, computer):
        return"You win!"
    return"You lost!"

def who_wins(player,computer):
    #r>s,p>r,s>p
    if (player=='r' and computer=='s') or (player=='s' and computer=='p') or (player=='p' and computer=='r'):
        return True    

print(play())