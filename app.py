from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello welcome my project CI/CD with GitHub Actions & Docker Hub in Digital Skola (DevOps Engineering)"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
