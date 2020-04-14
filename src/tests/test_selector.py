#!/usr/bin/env python3

import unittest
import os
from src.main import selector


class SelectorTest(unittest.TestCase):
    def setUp(self):
        self.movies = [
            "movie 1",
            "another movie",
            "a good movie",
            "a bad movie",
            "terrible movie",
        ]
        self.filename = "test_file.csv"
        with open(self.filename, "w") as f:
            [f.write("{}\n".format(x)) for x in self.movies]

    def tearDown(self):
        os.remove(self.filename)

    def test_selects_movie_from_list(self):
        movie = selector.choose(self.movies)

        self.assertIn(movie, self.movies)
        self.assertIsInstance(movie, str)

    def test_converts_a_path_to_a_csv_into_a_list_with_contents_of_the_file(self):
        contents = selector.read_csv(self.filename)

        self.assertIsInstance(contents, list)
        self.assertEqual(contents, self.movies)


if __name__ == "__main__":
    unittest.main()
