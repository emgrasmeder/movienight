FROM python:3.8-slim

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src ./src
COPY resources ./resources

EXPOSE 5000

#ENTRYPOINT ["tail", "-f", "/dev/null"]
#ENTRYPOINT ["python", "src/main/selector.py", "resources/movies.csv"]
CMD ["python", "src/main/server.py"]
