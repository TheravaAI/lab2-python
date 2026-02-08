"""
Program Name: Deal Cards
Author: Hibo Jama
Purpose: This program simulates dealing a hand of cards. The user selects how many
cards they want, and the program randomly generates that many unique cards
without repeats.
Starter Code: None
Date: 2/7/2026
"""

import random

values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["c", "h", "s", "d"]

num_cards = int(input("How many cards would you like to be dealt? "))

hand = []

while len(hand) < num_cards:
    value = random.choice(values)
    suit = random.choice(suits)
    card = value + suit

    if card not in hand:
        hand.append(card)

print("\nYour hand:")
for card in hand:
    print(card)

print("\nTotal number of cards dealt:", len(hand))
