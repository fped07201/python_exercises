def validateInput(option):
    if option not in ["rock", "paper", "scissors"]:
        print('Invalid option: ' + option)
        return False
    return True

continue_flag = 'y'
while continue_flag=='y':
    print("Welcome to Rock, Paper, Scissors game.")
    player1 = input("Player1 enter your play (rock, paper, scissors): ").lower()
    player2 = input("Player2 enter your play (rock, paper, scissors): ").lower()
    if validateInput(player1) and validateInput(player2):
        if player1 == player2:
            print("No one wins!")
        elif player1 <= player2:
            print("Player1 wins!!!")
        else:
            print("Player2 wins!!!")

    continue_flag = input("Continue playing? Press 'y' to continue or any other key to stop: ").lower()
    
