"""
Program Name: String Manipulator
Author: Hibo Jama
Purpose: This program takes a message from the user, displays the original message,
         the reversed message, and the number of characters in the message.
Date: 01/27/2026
"""
print("This program will take a message and display it forwards and backwards.")

message = input("Please enter a message: ")

reversed_message = message[::-1]

print(f"Original message: {message}")
print(f"Reversed message: {reversed_message}")
print(f"The original message contains {len(message)} characters.")
