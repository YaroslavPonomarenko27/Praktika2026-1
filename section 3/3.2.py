from flask import Flask, jsonify, request

app = Flask(__name__)

# Простий ресурс
tasks = [{"id": 1, "task": "Learn Python"}]

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    new_task = request.json
    tasks.append(new_task)
    return jsonify(new_task), 201

if __name__ == "__main__":
    app.run(debug=True)
