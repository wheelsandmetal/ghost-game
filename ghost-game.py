import os
from random import randint


def show_word_alone(word, player):
    input(f"Player {player} press enter when no one else can see the screen")
    print(word)
    input("Press enter to clear screen")
    os.system('clear')


def assigning_roles(word, n_players):
    ghost = randint(1, n_players)
    for i in range(n_players):
        if i == ghost:
            show_word_alone("ghost", i)
        else:
            show_word_alone(word, i)


def main():
    n_players = int(input("Number of players: "))
    word = input("What's your secret word: ")
    input("Press Enter to continue...")
    os.system('clear')
    assigning_roles(word, n_players)


if __name__ == "__main__":
    main()
