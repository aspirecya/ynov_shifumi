import os
import random


def menu():
    print("1. one player")
    print("2. two players")

    selection = input()

    if selection == "1":
        os.system('clear')
        oneplayer()
    elif selection == "2":
        os.system('clear')
        twoplayers()
    else:
        exit()


def twoplayers():
    p1_score = 0
    p2_score = 0

    while p1_score != 3 and p2_score != 3:
        print("Player 1 score:", p1_score, "- Player 2 score:", p2_score)
        print("Choose Rock Paper or Scissors.\n")
        player1 = input("Player 1: ")
        os.system('clear')
        player2 = input("Player 2: ")
        os.system('clear')
        print("Player 1 choice:", player1, "- Player 2 choice:", player2)

        # p1 wins scenarios
        if player1 == 'rock' and player2 == 'scissors':
            print("Player 1 wins.")
            p1_score += 1
        elif player1 == 'paper' and player2 == 'rock':
            print("Player 1 wins.")
            p1_score += 1
        elif player1 == 'scissors' and player2 == 'paper':
            print("Player 1 wins.")
            p1_score += 1
        # p2 wins scenarios
        elif player1 == 'rock' and player2 == 'paper':
            print("Player 2 wins.")
            p2_score += 1
        elif player1 == 'paper' and player2 == 'scissors':
            print("Player 2 wins.")
            p2_score += 1
        elif player1 == 'scissors' and player2 == 'rock':
            print("Player 2 wins.")
            p2_score += 1
        # ties scenario
        elif player1 == 'rock' and player2 == 'rock':
            print("It's a tie")
        elif player2 == 'scissors' and player2 == 'scissors':
            print("It's a tie")
        elif player1 == 'paper' and player2 == 'paper':
            print("It's a tie")


def oneplayer():
    p1_score = 0
    p2_score = 0
    choices = {'rock': '1', 'paper': '2', 'scissors': '3'}

    while p1_score != 3 and p2_score != 3:
        print("Player 1 score:", p1_score, "- Computer score:", p2_score)
        print("Choose Rock Paper or Scissors.\n")
        player1 = input("Player 1: ")
        player2 = random.choice(list(choices.keys()))
        os.system('clear')
        print("Player 1 choice:", player1, "- Computer choice:", player2)

        # p1 wins scenarios
        if player1 == 'rock' and player2 == 'scissors':
            print("Player 1 wins.")
            p1_score += 1
        elif player1 == 'paper' and player2 == 'rock':
            print("Player 1 wins.")
            p1_score += 1
        elif player1 == 'scissors' and player2 == 'paper':
            print("Player 1 wins.")
            p1_score += 1
        # IA wins scenarios
        elif player1 == 'rock' and player2 == 'paper':
            print("Computer wins.")
            p2_score += 1
        elif player1 == 'paper' and player2 == 'scissors':
            print("Computer wins.")
            p2_score += 1
        elif player1 == 'scissors' and player2 == 'rock':
            print("Computer wins.")
            p2_score += 1
        # ties scenario
        elif player1 == 'rock' and player2 == 'rock':
            print("It's a tie")
        elif player2 == 'scissors' and player2 == 'scissors':
            print("It's a tie")
        elif player1 == 'paper' and player2 == 'paper':
            print("It's a tie")


menu()
