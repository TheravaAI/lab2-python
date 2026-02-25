"""
Program Name: User Login System
Author: Hibo Jama
Purpose: This program simulates a basic user login system using a dictionary
         to store usernames and passwords. It verifies user credentials and
         assigns a security level based on the username.
Starter Code: None
Date: February 23, 2026
"""

# Dictionary storing usernames and passwords
users = {
    "gwalters": "S3curePass!",
    "admin": "Admin123",
    "jdoe": "Password!",
    "guest": "guest"
}

# Ask for username
username = input("Enter username: ")

# Check if username exists
if username not in users:
    print("\nUser not found. Exiting.")
    exit()

# Ask for password
password = input("Enter password: ")

# Check password
if password == users[username]:
    if username == "guest":
        security_level = "Guest access"
    else:
        security_level = "Security Level 1"

    print(f"\nWelcome, {username}. You have {security_level}.")
else:
    print("\nAccess Denied.")