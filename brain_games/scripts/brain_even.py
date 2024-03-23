#!/usr/bin/env python3
from brain_games.games import brain_even_logic as play_brain_even
from brain_games.engine.engine import engine


def main():
    engine(play_brain_even)


if __name__ == '__main__':
    main()
