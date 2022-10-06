from time import time

import pytest

from movie_night import filters, selector


@pytest.fixture
def a_movie_with_timestamp():
    return [f"movie 1, {int(time())}"]


def test_returns_only_unseen_movies(a_movie_with_timestamp):
    movie = selector.choose(a_movie_with_timestamp, filters.seen_movie_filter)

    assert movie == ""


def test_filters_old_timestamps():
    other_movies = ["movie, 999", f"movie2, {int(time())}"]

    filtered_movies = list(filter(filters.seen_movie_filter, other_movies))

    assert filtered_movies == ["movie, 999"]
