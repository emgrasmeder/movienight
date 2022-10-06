# movie-night
let's not fight over choosing a movie anymore

this baby app chooses a movie from your movie list at random and can filter too

### install dependencies
`poetry install`

### run
`python movie_night/selector.py resources/movies.csv`

### run tests
`./run.sh unit_test`

### run in docker
docker build --tag movie-night-app .
docker run -p 80:80 movie-night-app
