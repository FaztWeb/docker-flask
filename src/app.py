from flask import Flask, jsonify
from users import users

app = Flask(__name__)

# Routes
@app.route("/", methods=["GET"])
def ping():
    return jsonify({"response": "pong!"})


@app.route("/users")
def usershandler():
    return jsonify({"users": users})

# Start the Server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
