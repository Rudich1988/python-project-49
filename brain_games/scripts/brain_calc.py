#!/usr/bin/env python3
from brain_games.games import brain_calc_logic as play_brain_calc
from brain_games.games.engine import engine


def main():
    engine(play_brain_calc)


if __name__ == '__main__':
    main()
