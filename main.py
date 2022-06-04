import random
import math
from unittest import result


def play():
    player = input("what's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    player = player.lower

    computer = random.choice(['r', 'p', 's'])

    if player == computer:
        return (0, player, computer)

    #   r > s, s > p, p > r
    if it_win(player, computer):
        return (1, player, computer)

    return (-1, player, computer)


def it_win(player, computer):
    # return true is the player beats the opponent
    # winning conditions: r > s, s > p, p > r
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (
            player == 'p' and computer == 'r'):
        return True
    return False

def play_best_of(n):
    # play against the computer until someone wins
    # to win you must win cell(n/2)games
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, player, computer = play()
       # tie
        if result == 0:
            print('it is a tie. you and the computer have both chosen{}. \n'.format(player))
       # you win
        elif result == 1:
            player_wins += 1
            print('you chose{} and the computer chose{}. you win!\n'.format(player, computer))
        else:
            computer_wins += 1
            print('you chose{} and the computer chose{}. you lose :(\n'.format(player, computer))
        print('\n')
        if player_wins > computer_wins:
            print('you have won the best of {}games! did well :D')
        else:
            print('sorry you lose, the computer has won the best of {}games. Better luck next time!'.format(n))


if __name__ == '__main__':
    play_best_of(3)