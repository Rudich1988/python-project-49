#!/usr/bin/env python3
from brain_games.games import brain_progression as play_brain_progression
from brain_games.engine.engine import start_game


def main():
    start_game(play_brain_progression)


if __name__ == '__main__':
    main()
