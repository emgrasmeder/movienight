#!/usr/bin/env python3

import unittest
import os
from time import time
from src.main import selector
from src.main import filters


class FilterTest(unittest.TestCase):
    def setUp(self):
        self.movies = ["movie 1, {}".format(int(time()))]
        self.filename = "test_file.csv"
        with open(self.filename, "w") as f:
            [f.write("{}\n".format(x)) for x in self.movies]

    def tearDown(self):
        os.remove(self.filename)

    def test_returns_only_unseen_movies(self):
        movie = selector.choose(self.movies, filters.seen_movie_filter)

        self.assertEqual(movie, "")

    def test_filters_old_timestamps(self):
        other_movies = ["movie, 999", "movie2, {}".format(int(time()))]

        filtered_movies = list(filter(filters.seen_movie_filter, other_movies))

        self.assertEqual(filtered_movies, ["movie, 999"])


if __name__ == "__main__":
    unittest.main()
