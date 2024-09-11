from flask import Flask, request, jsonify

app = Flask(__name__)

todos = [
    {"label": "My first Task", "done": False}
]


@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)


@app.route('/todos', methods=['POST'])
def add_new_todo(): 
    request_body = request.get_json(force=True)
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos), 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    try:
        todos.pop(position)
        return jsonify(todos), 200
    except IndexError:
        return jsonify({"error": "Invalid position"}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)