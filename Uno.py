print("Welcome to the game of Uno!!!")
print("you can play in 1-4 players")
players = int(input("Choose the number of players:"))






# Define the card types and their counts
Cards = {
    "Number_cards": {
        color: [[0], list(range(1, 10)), list(range(1, 10))] for color in ["Red", "Blue", "Green", "Yellow"]
    },
    "Action_cards": {
        action: [1, 2, 3, 4] for action in ["Reverse", "Skip", "Draw_2"]
    },
    "Wild_cards": {
        wild: [1, 2, 3, 4] for wild in ["Clr_Change", "Clr_Change_Draw_4"]
    }
}

