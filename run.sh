#!/usr/bin/env bash

__dev_server(){
  (
  app="movie_night_app"
  docker stop ${app}
  docker rm ${app}
  docker build -t ${app} .
  docker run -d -p 5000:5000 \
    --name=${app} \
    -v $PWD:/app ${app}
  )
}

__end_to_end_test() {
  (
    cd tests/
    echo "I'm in folder $(pwd)"
    echo "Tests should run here"
  )
}

__unit_test() {
  (
    poetry run python3 -m pytest -v tests/test*.py
  )
}

validate_args() {
  acceptable_args="$(declare -F | sed -n "s/declare -f __//p" | tr '\n' ' ')"

  if [[ -z $1 ]]; then
    echo "Must provide an argument"
    echo -e "Available commands:\n$(declare -F | sed -n "s/declare -f __/ - /p")"
    exit 1
  fi
  if [[ ! " $acceptable_args " =~ .*\ $1\ .* ]]; then
    echo "Invalid argument: $1"
    echo -e "Available commands:\n$(declare -F | sed -n "s/declare -f __/ - /p")"
    exit 1
  fi
}

CMD=${1:-}
shift || true
if validate_args ${CMD}; then
  __${CMD}
  exit 0
fi
