FROM python:3.8-slim-buster

COPY requirements.txt .

RUN pip install --quiet -r requirements.txt

COPY src ./src
COPY resources ./resources

#ENTRYPOINT ["tail", "-f", "/dev/null"]
ENTRYPOINT ["python", "src/main/selector.py", "resources/movies.csv"]
