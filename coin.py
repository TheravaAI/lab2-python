"""
Program Name: Coin Class
Author: Hibo Jama
Purpose: This class represents a coin that can be tossed and shows either Heads or Tails.
Starter Code: None
Date: 3/24/26
"""

import random

class Coin:
    def __init__(self):
        self.__sideup = "Heads"

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        return self.__sideup