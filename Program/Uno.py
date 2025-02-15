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
# import pygame
# import random

# # Initialize Pygame
# pygame.init()

# # Screen settings
# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("UNO Game - 2 Player")

# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# YELLOW = (255, 255, 0)
# GRAY = (169, 169, 169)

# # Load card images
# CARD_WIDTH, CARD_HEIGHT = 80, 120
# FPS = 60
# clock = pygame.time.Clock()

# # Card attributes
# COLORS = ["Red", "Green", "Blue", "Yellow"]
# VALUES = list(range(0, 10)) + ["Skip", "Reverse", "Draw Two"]
# SPECIAL_CARDS = ["Wild", "Wild Draw Four"]

# def generate_deck():
#     deck = []
#     for color in COLORS:
#         for value in VALUES:
#             deck.append((color, value))
#             if value != 0:
#                 deck.append((color, value))
#     for special in SPECIAL_CARDS:
#         deck.extend([(None, special)] * 4)
#     random.shuffle(deck)
#     return deck

# NUM_PLAYERS = 2
# players = {i: [] for i in range(NUM_PLAYERS)}
# deck = generate_deck()

# def draw_card_animation():
#     for i in range(10):
#         screen.fill(WHITE)
#         pygame.draw.rect(screen, GRAY, (WIDTH//2 - 40, HEIGHT//2 - 60, CARD_WIDTH, CARD_HEIGHT))
#         pygame.display.flip()
#         clock.tick(30)

# def draw_card_for_player(player):
#     if deck:
#         draw_card_animation()
#         players[player].append(deck.pop())

# for _ in range(7):
#     for i in range(NUM_PLAYERS):
#         players[i].append(deck.pop())

# discard_pile = [deck.pop()]
# turn = 0
# reverse = False
# running = True
# font = pygame.font.Font(None, 36)

# def draw_text(text, x, y, color=BLACK):
#     label = font.render(text, True, color)
#     screen.blit(label, (x, y))

# def draw_card(card, x, y):
#     color, value = card
#     pygame.draw.rect(screen, RED if color == "Red" else GREEN if color == "Green" else BLUE if color == "Blue" else YELLOW, (x, y, CARD_WIDTH, CARD_HEIGHT))
#     draw_text(str(value), x + 20, y + 40, WHITE)

# def get_playable_cards(hand, top_card):
#     color, value = top_card
#     return [card for card in hand if card[0] == color or card[1] == value or card[0] is None]

# def draw_game():
#     screen.fill(WHITE)
    
#     # Draw top card of discard pile
#     draw_card(discard_pile[-1], WIDTH//2 - 40, HEIGHT//2 - 60)
    
#     x_offset = 50
#     for card in players[turn]:
#         draw_card(card, x_offset, 450 if turn == 0 else 150)
#         x_offset += CARD_WIDTH + 10
    
#     pygame.draw.rect(screen, GRAY, (WIDTH//2 - 40, HEIGHT//2, CARD_WIDTH, CARD_HEIGHT))
#     draw_text("Draw", WIDTH//2 - 20, HEIGHT//2 + 50, BLACK)
    
#     pygame.display.flip()

# def check_card_click(mouse_x, mouse_y):
#     x_offset = 50
#     for index, card in enumerate(players[turn]):
#         if x_offset <= mouse_x <= x_offset + CARD_WIDTH and (450 if turn == 0 else 150) <= mouse_y <= (450 if turn == 0 else 150) + CARD_HEIGHT:
#             return index
#         x_offset += CARD_WIDTH + 10
#     if WIDTH//2 - 40 <= mouse_x <= WIDTH//2 + 40 and HEIGHT//2 <= mouse_y <= HEIGHT//2 + CARD_HEIGHT:
#         return "draw"
#     return None

# while running:
#     screen.fill(WHITE)
#     draw_game()
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             mouse_x, mouse_y = event.pos
#             selected_card_index = check_card_click(mouse_x, mouse_y)
#             if selected_card_index == "draw":
#                 draw_card_for_player(turn)
#             elif isinstance(selected_card_index, int):
#                 selected_card = players[turn][selected_card_index]
#                 if selected_card in get_playable_cards(players[turn], discard_pile[-1]):
#                     players[turn].remove(selected_card)
#                     discard_pile.append(selected_card)
#                     turn = (turn + 1) % NUM_PLAYERS
    
#     pygame.display.update()
#     clock.tick(FPS)

# pygame.quit()
"""uno text based"""
# import random

# # Card attributes
# COLORS = ["Red", "Green", "Blue", "Yellow"]
# VALUES = list(range(0, 10)) + ["Skip", "Reverse", "Draw Two"]
# SPECIAL_CARDS = ["Wild", "Wild Draw Four"]

# def generate_deck():
#     deck = []
#     for color in COLORS:
#         for value in VALUES:
#             deck.append((color, value))
#             if value != 0:
#                 deck.append((color, value))
#     for special in SPECIAL_CARDS:
#         deck.extend([(None, special)] * 4)
#     random.shuffle(deck)
#     return deck

# def get_playable_cards(hand, top_card):
#     color, value = top_card
#     return [card for card in hand if card[0] == color or card[1] == value or card[0] is None]

# def play_uno(num_players):
#     players = {i: [] for i in range(num_players)}
#     deck = generate_deck()
#     discard_pile = [deck.pop()]
    
#     for _ in range(7):
#         for i in range(num_players):
#             players[i].append(deck.pop())
    
#     turn = 0
#     reverse = False
    
#     while True:
#         print(f"\nTop card: {discard_pile[-1]}")
#         print(f"Player {turn+1}'s turn. Your hand: {players[turn]}")
        
#         playable_cards = get_playable_cards(players[turn], discard_pile[-1])
#         if playable_cards:
#             print(f"Playable cards: {playable_cards}")
#             choice = int(input("Select a card index to play: "))
#             selected_card = players[turn].pop(choice)
#             discard_pile.append(selected_card)
            
#             if selected_card[1] == "Reverse":
#                 reverse = not reverse
#             elif selected_card[1] == "Skip":
#                 turn = (turn + (1 if not reverse else -1)) % num_players
#             elif selected_card[1] == "Draw Two":
#                 next_turn = (turn + (1 if not reverse else -1)) % num_players
#                 players[next_turn].extend([deck.pop(), deck.pop()])
#             elif selected_card[1] == "Wild" or selected_card[1] == "Wild Draw Four":
#                 new_color = input("Choose a color (Red, Green, Blue, Yellow): ")
#                 discard_pile.append((new_color, selected_card[1]))
#                 if selected_card[1] == "Wild Draw Four":
#                     next_turn = (turn + (1 if not reverse else -1)) % num_players
#                     players[next_turn].extend([deck.pop(), deck.pop(), deck.pop(), deck.pop()])
#         else:
#             print("No playable cards. Drawing a card...")
#             players[turn].append(deck.pop())
        
#         if not players[turn]:
#             print(f"Player {turn+1} wins!")
#             break
        
#         turn = (turn + (1 if not reverse else -1)) % num_players

# # Start game
# num_players = int(input("Enter number of players (2-4): "))
# if 2 <= num_players <= 4:
#     play_uno(num_players)
# else:
#     print("Invalid number of players. Exiting.")
