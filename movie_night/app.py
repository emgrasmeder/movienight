from fastapi import FastAPI
from uvicorn import run
import selector

app = FastAPI()


@app.get("/")
def root():
    movie = selector.choose(selector.read_csv("resources/movies.csv"))
    return f"Tonight we watch: {movie}!"


if __name__ == "__main__":
    run("app:app", host="0.0.0.0", port=80, reload=True)
