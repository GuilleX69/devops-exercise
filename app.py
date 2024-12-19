from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Initialize the counter for POST requests
post_request_count = 0

@app.route("/")
def home():

    return render_template("index.html")

@app.route("/increment", methods=["POST"])
def increment_counter():

    global post_request_count
    post_request_count += 1
    return jsonify({"message": "Counter incremented"})

@app.route("/counter", methods=["GET"])
def get_counter():

    return jsonify({"counter": post_request_count})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
