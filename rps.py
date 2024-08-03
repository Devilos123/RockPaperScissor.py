import random

def get_computer_choice():
    """Randomly choose rock, paper, or scissors for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    """Determine the winner of the game."""
    if player_choice == computer_choice:
        return 'It\'s a tie!'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return 'You win!'
    else:
        return 'You lose!'

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to make your choice.")
    
    player_choice = input("Your choice: ").lower()
    while player_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
        player_choice = input("Your choice: ").lower()
    
    computer_choice = get_computer_choice()
    print(f"The computer chose: {computer_choice}")
    
    result = determine_winner(player_choice, computer_choice)
    print(result)

# Run the game
rock_paper_scissors()
