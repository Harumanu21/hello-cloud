from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Im Daman and Rishi from bca5!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
