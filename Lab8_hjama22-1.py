"""
Program Name: Lab8_hjama22-1.py
Author: Hibo Jama
Purpose: This program validates a 12-digit UPC-A code by calculating
         the correct check digit and comparing it with the provided one.
Starter Code: None
Date: March 10, 2026
"""

def find_UPC(first11):

    odd_sum = 0
    even_sum = 0

    for i in range(len(first11)):
        digit = int(first11[i])

        if i % 2 == 0:
            odd_sum += digit
        else:
            even_sum += digit

    total = (odd_sum * 3) + even_sum
    check_digit = (10 - (total % 10)) % 10

    return check_digit


def main():

    while True:
        upc = input("Enter a 12-digit UPC: ")

        if len(upc) != 12 or not upc.isdigit():
            print("Error: UPC must be exactly 12 digits.\n")
            continue
        break

    first11 = upc[:11]
    provided_digit = int(upc[11])

    print(f"\nThe first 11 digits are '{first11}'.")
    print(f"The provided check digit is '{provided_digit}'.\n")

    print("Calculating...")

    expected_digit = find_UPC(first11)

    print(f"The expected check digit is {expected_digit}.\n")

    if expected_digit == provided_digit:
        print("This is a VALID UPC.")
    else:
        print("This is an INVALID UPC.")


if __name__ == "__main__":
    main()