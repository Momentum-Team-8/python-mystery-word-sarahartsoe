import random

EASY_WORDS = [
    'bang', 'seed', 'sell', 'inch', 'firm', 'meal', 'mess', 'rate', 'fill', 'goal', 'full', 'fade', 'herb', 'body', 'goat', 'disk', 'rich', 'silk', 'plot', 'gene', 'riot', 'zero', 'cast', 'dose', 'stun',
    'throw', 'drift', 'tease', 'sweat', 'siege', 'irony', 'vague', 'spell', 'young', 'brain', 'color', 'spill', 'forge', 'glory', 'torch', 'slant', 'yearn', 'bacon', 'board', 'spine', 'width', 'enjoy', 'drama', 'wound',
]

NORM_WORDS = [
    'stable', 'insure', 'sermon', 'candle', 'suntan', 'rabbit', 'origin', 'cancel', 'waiter', 'stress', 'attack', 'deadly', 'debate', 'reform', 'prayer', 'master', 'safety', 'castle', 'reward', 'linear', 'horror', 'tumble', 'export', 'matter', 'tumour',
    'appoint', 'package', 'brother', 'pudding', 'premium', 'trainer', 'feeling', 'realize', 'balance', 'meaning', 'private', 'account', 'quarrel', 'dribble', 'abandon', 'overeat', 'rainbow', 'concede', 'command', 'silence', 'musical', 'railcar', 'warrant', 'peasant', 'opinion',
]

HARD_WORDS = [
    'correction', 'conviction', 'monopoly', 'patience', 'uncertainty', 'acceptance', 'confusion', 'conception', 'analysis', 'pleasure', 'regulation', 'threshold', 'transmission', 'interface', 'notebook', 'priority', 'neighbour', 'horseshoe', 'vegetable', 'ambition', 'philosophy', 'crosswalk', 'judgment', 'execution', 'transaction', 'comfortable', 'commission', 'elaborate',
    'parameter', 'identity', 'exclusive', 'understand', 'translate', 'chauvinist', 'withdrawl', 'evolution', 'domestic', 'catalogue', 'conversation', 'coalition', 'competence', 'freighter', 'cooperative', 'abundant', 'blackmail', 'isolation', 'communist', 'infinite', 'treasurer', 'governor',
]

print("Do you have what it takes to find the mystery word?")
print("Choose a level- ")
print("Easy is 4-5 letters")
print("Normal is 6-7 letters")
print("Hard is 8+ letters")
print("You have 8 guesses - guess one letter per try.")
print("Game over when you guess the word or run out of tries!")
print("Good luck and DON'T fuck it up!")

level = input("Choose your level. Enter 1 for Easy, 2 for Normal, or 3 for Hard: ")
if level == "1":
    wordChoice = (random.choice(EASY_WORDS))
if level == "2":
    wordChoice = (random.choice(NORM_WORDS))
if level == "3":
    wordChoice = (random.choice(HARD_WORDS))
    
def mystery_word_game():
    tries = 0
    test = wordChoice
    word_list = []
    
    # word_guess = ""
    for x in test:
        word_list.append(x)
    print(test)
    
    correct_guesses = []
    incorrect_guesses = []
    while tries != 8:
        current_progress = []
        tries += 1
        player_guess = input("Good choice! What letter do you guess? ")
        if len(player_guess) > 1:
            print("Your guess must be one letter!")
            player_guess = input("Good choice! What letter do you guess? ")
        
        for x in word_list: 
            if player_guess == x:
                current_progress.append(player_guess)
                correct_guesses.append(player_guess)
            elif x in correct_guesses:
                current_progress.append(x)
            else:
                current_progress.append("_")
                incorrect_guesses.append(player_guess)
        while tries == 8:
            print("You lose! Your word was: " + test)
            break
        print(current_progress)




mystery_word_game()




# guesses = ''   

# tries = 8

# while tries > 0:
#     lost = 0
#     for letter in wordChoice:
#         if letter in guesses:
#             print(letter)
#         else:
#             print("_")
#             lost += 1
#     if lost == 0:
#         print("Good job!")
#     break

# guess = input("Good choice! What letter do you guess? ")
# if len(letter) >= 2:
#         print("Your guess can only be one letter!")
# guesses += guess
# if guess not in wordChoice:
#     tries -= 1