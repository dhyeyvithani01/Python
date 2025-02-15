# def main():
#     print("Welcome to the game of Uno!!!")
#     print("you can play in 1-4 players")
#     players = int(input("Choose the number of players:"))
# Colors=["Red","Blue","Green","Yellow"]
# Num=list(range(0,9))
# Actions = ["Reverse","Skip",""]


"""Ai game uno"""
# import random

# # Card colors and values
# COLORS = ["Red", "Green", "Blue", "Yellow"]
# VALUES = list(range(0, 10)) + ["Skip", "Reverse", "Draw Two"]
# SPECIAL_CARDS = ["Wild", "Wild Draw Four"]

# # Generate a deck of UNO cards
# def generate_deck():
#     deck = []
#     for color in COLORS:
#         for value in VALUES:
#             deck.append((color, value))
#             if value != 0:
#                 deck.append((color, value))  # Each number/action card appears twice
#     for special in SPECIAL_CARDS:
#         deck.extend([(None, special)] * 4)  # Wild cards (colorless)
#     random.shuffle(deck)
#     return deck

# # Initialize game
# NUM_PLAYERS = 4
# players = {i: [] for i in range(NUM_PLAYERS)}
# deck = generate_deck()

# # Distribute initial cards
# for _ in range(7):
#     for i in range(NUM_PLAYERS):
#         players[i].append(deck.pop())

# # Game state variables
# discard_pile = [deck.pop()]
# turn = 0
# reverse = False

# # Function to get playable cards
# def get_playable_cards(hand, top_card):
#     color, value = top_card
#     playable = [card for card in hand if card[0] == color or card[1] == value or card[0] is None]
#     return playable

# # Function to change turn
# def next_turn():
#     global turn
#     if reverse:
#         turn = (turn - 1) % NUM_PLAYERS
#     else:
#         turn = (turn + 1) % NUM_PLAYERS

# # Game loop
# while True:
#     current_player = players[turn]
#     top_card = discard_pile[-1]
    
#     playable_cards = get_playable_cards(current_player, top_card)
#     if playable_cards:
#         chosen_card = random.choice(playable_cards)  # AI chooses a random valid card
#         current_player.remove(chosen_card)
#         discard_pile.append(chosen_card)
#         print(f"Player {turn} plays {chosen_card}")
        
#         # Handle special cards
#         if chosen_card[1] == "Reverse":
#             reverse = not reverse
#         elif chosen_card[1] == "Skip":
#             next_turn()
#         elif chosen_card[1] == "Draw Two":
#             next_turn()
#             players[turn].extend([deck.pop() for _ in range(2)])
#         elif chosen_card[1] == "Wild" or chosen_card[1] == "Wild Draw Four":
#             chosen_color = random.choice(COLORS)
#             discard_pile[-1] = (chosen_color, chosen_card[1])
#             if chosen_card[1] == "Wild Draw Four":
#                 next_turn()
#                 players[turn].extend([deck.pop() for _ in range(4)])
#     else:
#         drawn_card = deck.pop()
#         current_player.append(drawn_card)
#         print(f"Player {turn} draws a card")
    
#     # Check for winner
#     if not current_player:
#         print(f"Player {turn} wins!")
#         break
    
#     next_turn()
"""text based uno"""
# import random

# # Card colors and values
# COLORS = ["Red", "Green", "Blue", "Yellow"]
# VALUES = list(range(0, 10)) + ["Skip", "Reverse", "Draw Two"]
# SPECIAL_CARDS = ["Wild", "Wild Draw Four"]

# # Generate a deck of UNO cards
# def generate_deck():
#     deck = []
#     for color in COLORS:
#         for value in VALUES:
#             deck.append((color, value))
#             if value != 0:
#                 deck.append((color, value))  # Each number/action card appears twice
#     for special in SPECIAL_CARDS:
#         deck.extend([(None, special)] * 4)  # Wild cards (colorless)
#     random.shuffle(deck)
#     return deck

# # Initialize game
# NUM_PLAYERS = int(input("Enter number of players: "))
# players = {i: [] for i in range(NUM_PLAYERS)}
# deck = generate_deck()

# # Distribute initial cards
# for _ in range(7):
#     for i in range(NUM_PLAYERS):
#         players[i].append(deck.pop())

# # Game state variables
# discard_pile = [deck.pop()]
# turn = 0
# reverse = False

# # Function to get playable cards
# def get_playable_cards(hand, top_card):
#     color, value = top_card
#     playable = [card for card in hand if card[0] == color or card[1] == value or card[0] is None]
#     return playable

# # Function to change turn
# def next_turn():
#     global turn
#     if reverse:
#         turn = (turn - 1) % NUM_PLAYERS
#     else:
#         turn = (turn + 1) % NUM_PLAYERS

# # Game loop
# while True:
#     current_player = players[turn]
#     top_card = discard_pile[-1]
    
#     print(f"Top card: {top_card}")
#     print(f"Player {turn}'s turn. Your hand: {current_player}")
    
#     playable_cards = get_playable_cards(current_player, top_card)
#     if playable_cards:
#         print(f"Playable cards: {playable_cards}")
#         chosen_card = random.choice(playable_cards)  # AI chooses a random valid card
#         current_player.remove(chosen_card)
#         discard_pile.append(chosen_card)
#         print(f"Player {turn} plays {chosen_card}")
        
#         # Handle special cards
#         if chosen_card[1] == "Reverse":
#             reverse = not reverse
#         elif chosen_card[1] == "Skip":
#             next_turn()
#         elif chosen_card[1] == "Draw Two":
#             next_turn()
#             players[turn].extend([deck.pop() for _ in range(2)])
#         elif chosen_card[1] == "Wild" or chosen_card[1] == "Wild Draw Four":
#             chosen_color = random.choice(COLORS)
#             discard_pile[-1] = (chosen_color, chosen_card[1])
#             print(f"Player {turn} chooses color {chosen_color}")
#             if chosen_card[1] == "Wild Draw Four":
#                 next_turn()
#                 players[turn].extend([deck.pop() for _ in range(4)])
#     else:
#         drawn_card = deck.pop()
#         current_player.append(drawn_card)
#         print(f"Player {turn} draws a card")
    
#     # Check for winner
#     if not current_player:
#         print(f"Player {turn} wins!")
#         break
    
#     next_turn()
"""Gui based uno card"""
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("UNO Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Card attributes
COLORS = ["Red", "Green", "Blue", "Yellow"]
VALUES = list(range(0, 10)) + ["Skip", "Reverse", "Draw Two"]
SPECIAL_CARDS = ["Wild", "Wild Draw Four"]

# Generate a deck of UNO cards
def generate_deck():
    deck = []
    for color in COLORS:
        for value in VALUES:
            deck.append((color, value))
            if value != 0:
                deck.append((color, value))
    for special in SPECIAL_CARDS:
        deck.extend([(None, special)] * 4)
    random.shuffle(deck)
    return deck

# Initialize game
NUM_PLAYERS = 2
players = {i: [] for i in range(NUM_PLAYERS)}
deck = generate_deck()

# Distribute initial cards
for _ in range(7):
    for i in range(NUM_PLAYERS):
        players[i].append(deck.pop())

# Game state variables
discard_pile = [deck.pop()]
turn = 0
reverse = False
running = True
font = pygame.font.Font(None, 36)

def draw_text(text, x, y, color=BLACK):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

def draw_game():
    screen.fill(WHITE)
    draw_text(f"Top Card: {discard_pile[-1]}", 50, 50, RED)
    draw_text(f"Your Hand: {players[0]}", 50, 150, BLUE)
    pygame.display.flip()

# Game loop
while running:
    screen.fill(WHITE)
    draw_game()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()

pygame.quit()
