import random

def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    player_choice = input('Enter your choice (rock, paper, scissors): ')
    computer_choice = random.choice(choices)

    print('Your choice:', player_choice)
    print('Computer choice:', computer_choice)

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
            (player_choice == 'paper' and computer_choice == 'rock') or \
            (player_choice == 'scissors' and computer_choice == 'paper'):
        print('You win!')
    else:
        print('Computer wins!')

# Example usage
rock_paper_scissors()

















