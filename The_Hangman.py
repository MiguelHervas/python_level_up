import random


def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

def get_valid_letter(letters):
    letter = input()
    valid = False
    while not valid:
        if letter in letters:
            print("you already choosed that letter, Give me another one, please")
            letter = input()
        else:
            if len(letter) == 1 and not letter.isdigit():
                    return letter
                    valid = True
            else:
                print("That was not a valid letter, Give me another one, please")
                letter = input()

def update_progress(letters,progress,letter):
    for number_of_letter in range(len(letters)):
        if letters[number_of_letter] == letter:
            progress[number_of_letter] = letters[number_of_letter]

def print_the_progress(progress):
    progress_print = ""
    for letter in progress:
        progress_print = progress_print + letter
    print(progress_print)

def print_hangman(number_of_try):
    match number_of_try:
        case 0:
            print("  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========")
        case 1:
            print("  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========")
        case 2:
            print("  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========")
        case 3:
            print("  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========")
        case 4:
            print("  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========")
        case 5:
            print("  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========")
        case 6:
            print("  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========")



# Here you should put the path to your words file.
word = random_line('F:\Data Science\Python for ML\Python_Crazyness\words.txt')
letters = [*word]
user_progress = ["_","_","_","_","_"]
game_end = False
chosed_letters = [""]
fails = 0
while not game_end:
    print("Give me a letter")
    user_letter = get_valid_letter(chosed_letters)
    chosed_letters = chosed_letters + [user_letter]
    if user_letter in letters:
        update_progress(letters,user_progress,user_letter)
    else:
        print_hangman(fails)
        fails = fails + 1
    if letters == user_progress:
        print("you win, the word was:")
        game_end = True
    print("you have " + str(7-fails) + " trais left")
    print_the_progress(user_progress)
    if fails > 6:
        print("you loose, the word was:\n" + word)
        game_end = True






