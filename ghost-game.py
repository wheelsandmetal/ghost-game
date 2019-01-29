import os
from random import randint


def show_word_alone(word, player):
    input(
        f"Player {player} press enter when no one else can see the screen"
    )

    print(word)
    input("Press enter to clear screen")
    os.system('clear')


def assigning_roles(word, n_players):
    # The ghost can't be player 1
    ghost = randint(2, n_players)
    for i in range(1, n_players + 1):
        if i == ghost:
            show_word_alone("ghost", i)
        else:
            show_word_alone(word, i)


def main():
    n_players = int(input("Number of players: "))
    if n_players <= 1:
        print("You can't play by yourself.")
        return

    word = input("What's your secret word: ")
    os.system('clear')
    input("Press Enter to continue...")
    assigning_roles(word, n_players)


if __name__ == "__main__":
    main()
