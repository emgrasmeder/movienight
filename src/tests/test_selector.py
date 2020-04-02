#!/usr/bin/env python3

import unittest
from src.main import selector

class SelectorTest(unittest.TestCase):

    def test_selects_movie_from_list(self):
        movies = ["a", "n", "k", "h", "o"]

        movie = selector.choose(movies)

        self.assertIn(movie, movies)
        self.assertIsInstance(movie, str)
        

if __name__ == '__main__':
    unittest.main()
