from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>CI/CD Demo</h1>
    <p>Congratulations! Your Flask app is deployed successfully.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)