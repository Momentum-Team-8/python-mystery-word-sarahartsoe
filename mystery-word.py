import random


with open("words.txt") as f:
    word_list = f.read().splitlines()
    print(f)
    letter = input("What letter do you guess?")
    if len(letter) >= 2:
        print("Your guess can only be one letter!")