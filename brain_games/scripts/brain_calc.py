#!/usr/bin/env python3
from brain_games.games.brain_calc_logic import play_brain_calc
from brain_games.games.engine import engine


def main():
    engine(play_brain_calc)


if __name__ == '__main__':
    main()
