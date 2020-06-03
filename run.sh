#!/usr/bin/env bash

__dev_server(){
  (
  app="movienight_app"
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
    cd src/tests/
    echo "I'm in folder $(pwd)"
    echo "Tests should run here"
  )
}

__unittest() {
  (
    python3 -m unittest -v src/tests/test*.py
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
