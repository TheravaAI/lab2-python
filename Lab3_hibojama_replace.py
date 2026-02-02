"""
Program Name: Camping List - Replace Item
Author: Hibo Jama
Purpose: Replace one camping item with binoculars and
         display sections of the list using slice notation.
Starter Code: Imported from Lab3_hibojama_add.py
Date: 2/1/2026
"""

from Lab3_hibojama_add import camping_items

camping_items[5] = "binoculars"

binoculars_index = camping_items.index("binoculars")

print("Items before binoculars:")
print(camping_items[:binoculars_index])

print("Binoculars:")
print(camping_items[binoculars_index])

print("Items after binoculars:")
print(camping_items[binoculars_index + 1:])
