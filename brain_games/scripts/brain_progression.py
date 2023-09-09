#!/usr/bin/env python3
from brain_games.games.brain_progression_logic import (
    GAME_RULES,
    play_brain_progression,
)
from brain_games.games.engine import engine


def main():
    engine(play_brain_progression, GAME_RULES)


if __name__ == '__main__':
    main()
