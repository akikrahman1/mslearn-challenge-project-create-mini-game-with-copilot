# create a basic rock, paper, scissors game

import random

# keep a count of the player's wins and the computer's wins
player_wins = 0
computer_wins = 0

def play():

    # get user input
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")

        # validate the inputs, ensuring user only enters r, p, or s
    if user not in ['r', 'p', 's']:
        return 'Invalid input'

    # get computer input
    computer = random.choice(['r', 'p', 's'])

    # check who wins
    if user == computer:
        return 'It\'s a tie'
    
    return is_win(user, computer)


def is_win(player, opponent):
    global player_wins
    global computer_wins
  
    print(f'Player: {player}, Computer: {opponent}')

    # work out if player won using the rules of rock, paper, scissors
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        player_wins += 1
        return 'You won!'
    
    computer_wins += 1
    return 'You lost!'

# repeatedly play the game until user quits
while True:
    print(play())

    # print the player's and computer's wins
    print(f'Player wins: {player_wins}')
    print(f'Computer wins: {computer_wins}')

    # ask user if they want to play again
    if input('Do you want to play again? (y/n)\n') != 'y':
        break
