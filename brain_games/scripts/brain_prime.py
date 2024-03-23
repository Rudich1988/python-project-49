#!/usr/bin/env python3
from brain_games.games import brain_prime as play_brain_prime
from brain_games.engine.engine import start_game


def main():
    start_game(play_brain_prime)


if __name__ == '__main__':
    main()
