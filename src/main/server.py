from flask import Flask
import selector


app = Flask(__name__)
@app.route("/")
def hello():
    return selector.choose(selector.read_csv("resources/movies.csv"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
