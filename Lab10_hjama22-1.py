"""
Program Name: Lab10_hjama22-1.py
Author: Hibo Jama
Purpose: This program allows the user to select a text file and analyzes
         the frequency of words using OOP, file handling, and string processing.
Starter Code: None
Date: March 28 2026
"""

from pathlib import Path
import string


class WordAnalyzer:

    def __init__(self, filepath):
        self._path = Path(filepath)
        self._frequencies = {}

    def process_file(self):
        try:
            if not self._path.exists():
                raise FileNotFoundError

            translator = str.maketrans('', '', string.punctuation)

            with self._path.open('r', encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    line = line.translate(translator)

                    words = line.split()

                    for word in words:
                        if word in self._frequencies:
                            self._frequencies[word] += 1
                        else:
                            self._frequencies[word] = 1

            return True

        except FileNotFoundError:
            print("Error: File not found.")
            return False

    def print_report(self):
        print()

        for word in sorted(self._frequencies.keys()):
            print(f"{word:<10} :: {self._frequencies[word]}")


def main():

    files = {
        "1": ("Princess of Mars", "princess_mars.txt"),
        "2": ("Tarzan", "Tarzan.txt"),
        "3": ("Treasure Island", "treasure_island.txt"),
        "4": ("Monte Cristo", "monte_cristo.txt")
    }

    while True:
        print("\n--- Word Analyzer ---")
        print("Please select a file to analyze:")

        for key, value in files.items():
            print(f"{key}. {value[0]}")

        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "5":
            print("\nGoodbye!")
            break

        elif choice in files:
            filename = files[choice][1]

            print(f"\nProcessing '{filename}'...\n")

            analyzer = WordAnalyzer(filename)

            if analyzer.process_file():
                analyzer.print_report()

        else:
            print("\nInvalid choice. Please select from 1-5.")

        input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()