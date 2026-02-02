"""
Program Name: Camping List - Remove Item
Author: Hibo Jama
Purpose: Remove binoculars from the camping list and display
         the final list and total number of items.
Starter Code: Imported from Lab3_hibojama_replace.py
Date: 2/1/2026
"""

from Lab3_hibojama_replace import camping_items

camping_items.remove("binoculars")

print("Final camping items list:")
print(camping_items)

print(f"Total items being brought on the camping trip: {len(camping_items)}")
