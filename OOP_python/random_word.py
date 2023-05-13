"""Pulls random words from a file.txt"""
from random import random


class WordFinder:
    def __init__(self, path):
            """Read dictionary and reports # items read."""

            dict_file = open(path)

            self.words = self.parse(dict_file)

            print(f"{len(self.words)} words read")

    def parse(self, dict_file):
            """Parse dict_file -> list of words."""

            return [w.strip() for w in dict_file]

    def random(self):
            """Return random word."""

            return random.choice(self.words)