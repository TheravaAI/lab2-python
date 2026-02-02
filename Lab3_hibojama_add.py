"""
Program Name: Camping List - Add Items
Author: Hibo Jama
Purpose: Import a camping list and add additional items,
         then print the list in reverse alphabetical order.
Starter Code: Imported from Lab3_hibojama_list.py
Date: 2/1/2026
"""

from Lab3_hibojama_list import camping_items

camping_items.append("matches")
camping_items.append("hat")
camping_items.append("sunscreen")
camping_items.append("knife")
camping_items.append("backpack")

print("Camping items reversed alphabetically:")
print(sorted(camping_items, reverse=True))
