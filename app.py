from flask import Flask, request, jsonify

app = Flask(__name__)

# Counter to track the number of POST requests
post_request_count = 0

@app.route("/", methods=["GET", "POST"])
def handle_requests():
    global post_request_count
    
    if request.method == "POST":
        # Increment the counter on POST requests
        post_request_count += 1
        return jsonify({"message": "POST request received"}), 201
    
    elif request.method == "GET":
        # Return the counter on GET requests
        return jsonify({"post_request_count": post_request_count}), 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

