from flask import Flask

app = Flask(__name__)


@app.get("/")
def home():
    return "This is home page"

if __name__ == '__main__':
    app.run()
