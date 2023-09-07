#!/usr/bin/env python3
from brain_games.games.brain_gcd_logic import play_brain_gcd
from brain_games.games.engine import engine


def main():
    engine(play_brain_gcd)


if __name__ == '__main__':
    main()
