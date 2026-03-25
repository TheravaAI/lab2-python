"""
Program Name: Character Class
Author: Hibo Jama
Purpose: This program models a simple video game character with basic attributes and actions.
Starter Code: None
Date: 3/24/26
"""

class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self, damage):
        self.health -= damage

    def heal(self, amount):
        self.health += amount

    def get_status(self):
        return f"{self.name} has {self.health} health and {self.strength} strength"