from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Counter to track the number of POST requests
post_request_count = 0

# HTML Template for the View
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            color: #333;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        h1 {
            font-size: 2.5rem;
            color: #0078d7;
            margin-top: 50px;
        }
        button {
            background-color: #0078d7;
            color: white;
            border: none;
            padding: 10px 20px;
            margin: 20px;
            font-size: 1rem;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #005bb5;
        }
        .report {
            margin-top: 20px;
            font-size: 1.2rem;
        }
    </style>
</head>
<body>
    <h1>Hello, World!</h1>
    <div>
        <button onclick="sendPostRequest()">Send POST Request</button>
        <button onclick="clearCounter()">Clear Counter</button>
    </div>
    <div class="report">
        <p>POST Counter: <span id="postCount">0</span></p>
    </div>
    <script>
        async function sendPostRequest() {
            await fetch("/", { method: "POST" });
            updatePostCount();
        }
        async function clearCounter() {
            await fetch("/clear", { method: "POST" });
            updatePostCount();
        }
        async function updatePostCount() {
            const response = await fetch("/");
            const data = await response.json();
            document.getElementById("postCount").textContent = data.post_request_count;
        }
        updatePostCount(); // Initialize the counter on page load
    </script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def handle_requests():
    global post_request_count

    if request.method == "POST":
        post_request_count += 1
        return jsonify({"message": "POST request received"}), 201

    elif request.method == "GET":
        return jsonify({"post_request_count": post_request_count}), 200

@app.route("/clear", methods=["POST"])
def clear_counter():
    global post_request_count
    post_request_count = 0
    return jsonify({"message": "Counter cleared"}), 200

@app.route("/view", methods=["GET"])
def view():
    return render_template_string(html_template)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
