from flask import Flask, jsonify, request, abort
from flask_cors import CORS, cross_origin
from taskDAO import taskDAO

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def index():
    return app.send_static_file('taskviewer.html')

@app.route('/tasks')
@cross_origin()
def getAll():
    return jsonify(taskDAO.getAll())

@app.route('/tasks/<int:id>')
@cross_origin()
def findById(id):
    task = taskDAO.findByID(id)
    if not task:
        abort(404)
    return jsonify(task)

@app.route('/tasks', methods=['POST'])
@cross_origin()
def create():
    if not request.json:
        abort(400)
    task = {
        "title": request.json.get("title"),
        "description": request.json.get("description"),
        "due_date": request.json.get("due_date"),
        "status": request.json.get("status", "Pending")
    }
    if not task["title"] or not task["description"] or not task["due_date"]:
        abort(400)
    return jsonify(taskDAO.create(task))

@app.route('/tasks/<int:id>', methods=['PUT'])
@cross_origin()
def update(id):
    foundTask = taskDAO.findByID(id)
    if not foundTask:
        abort(404)
    if not request.json:
        abort(400)

    reqJson = request.json

    # Update fields if present
    if 'title' in reqJson:
        foundTask['title'] = reqJson['title']
    if 'description' in reqJson:
        foundTask['description'] = reqJson['description']
    if 'due_date' in reqJson:
        foundTask['due_date'] = reqJson['due_date']
    if 'status' in reqJson:
        foundTask['status'] = reqJson['status']

    taskDAO.update(id, foundTask)
    return jsonify(foundTask)

@app.route('/tasks/<int:id>', methods=['DELETE'])
@cross_origin()
def delete(id):
    taskDAO.delete(id)
    return jsonify({"done": True})

if __name__ == '__main__':
    app.run(debug=True)
