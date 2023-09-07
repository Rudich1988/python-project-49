#!/usr/bin/env python3
from brain_games.games.brain_even_logic import play_brain_even
from brain_games.games.engine import engine


def main():
    engine(play_brain_even)


if __name__ == '__main__':
    main()
