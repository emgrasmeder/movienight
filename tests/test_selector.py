import pytest
from pathlib import Path
from movie_night import selector


@pytest.fixture
def a_movie_list():
    return [
        "movie 1",
        "another movie",
        "a good movie",
        "a bad movie",
        "terrible movie",
    ]


@pytest.fixture
def a_movies_file_path(a_movie_list):
    filename = "test_file.csv"
    with open(filename, "w") as f:
        [f.write(f"{m}\n") for m in a_movie_list]

    yield filename

    Path(filename).unlink()


def test_selects_movie_from_list(a_movie_list):
    movie = selector.choose(a_movie_list)

    assert movie in a_movie_list
    assert isinstance(movie, str)


def test_converts_path_to_csv_into_list_of_movies(a_movies_file_path, a_movie_list):
    contents = selector.read_csv(a_movies_file_path)

    assert isinstance(contents, list)
    assert contents == a_movie_list
