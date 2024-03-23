#!/usr/bin/env python3
from brain_games.games import brain_gcd_logic as play_brain_gcd
from brain_games.engine.engine import start_game


def main():
    start_game(play_brain_gcd)


if __name__ == '__main__':
    main()
