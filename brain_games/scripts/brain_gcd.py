#!/usr/bin/env python3
from brain_games.games.brain_gcd_logic import play_brain_gcd, GAME_RULES
from brain_games.games.engine import engine


def main():
    engine(play_brain_gcd, GAME_RULES)


if __name__ == '__main__':
    main()
