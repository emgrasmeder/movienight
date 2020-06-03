FROM python:3.8-slim
RUN apt-get -y update && apt-get -y upgrade && apt-get -y install libblas-dev liblapack-dev libatlas-base-dev gfortran

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src ./src
COPY resources ./resources

EXPOSE 5000

#ENTRYPOINT ["tail", "-f", "/dev/null"]
#ENTRYPOINT ["python", "src/main/selector.py", "resources/movies.csv"]
CMD ["python", "src/main/server.py"]
