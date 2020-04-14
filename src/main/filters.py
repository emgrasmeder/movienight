from time import time


def seen_movie_filter(movie):
    about_three_months = 8e6
    amount_of_time_required_since_last_viewing = about_three_months
    now = int(time())
    timestamp_of_last_viewing = int(movie.split(",")[-1])
    return (
        movie
        if now - timestamp_of_last_viewing > amount_of_time_required_since_last_viewing
        else None
    )
