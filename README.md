# movienight
let's not fight over choosing a movie anymore

this baby app chooses a movie from your movie list at random and can filter too

### install dependencies
`pip3 install -r requirements.txt`

### run
`python3 src/main/selector.py resources/movies.csv`

### run tests
`./run.sh unittest`

### run in docker
docker build --tag movienight .
docker run movienight -i
