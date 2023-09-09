#!/usr/bin/env python3
from brain_games.games.brain_prime_logic import play_brain_prime, GAME_RULES
from brain_games.games.engine import engine


def main():
    engine(play_brain_prime, GAME_RULES)


if __name__ == '__main__':
    main()
