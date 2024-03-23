#!/usr/bin/env python3
from brain_games.games import brain_calc_logic as play_brain_calc
from brain_games.engine.engine import start_game


def main():
    start_game(play_brain_calc)


if __name__ == '__main__':
    main()
