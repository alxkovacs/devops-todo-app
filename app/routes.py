from flask import Blueprint, request, jsonify
from .models import db, Todo, User
from datetime import datetime

todo_bp = Blueprint('todo_bp', __name__)
user_bp = Blueprint('user_bp', __name__)

@todo_bp.route('/', methods=['GET'])
def list_todos():
    todos = Todo.query.all()
    response = []
    for t in todos:
        response.append({
            'id': t.id,
            'title': t.title,
            'due_date': t.due_date.isoformat() if t.due_date else None,
            'tags': t.tags,
            'user_id': t.user_id
        })
    return jsonify(response), 200

@todo_bp.route('/', methods=['POST'])
def add_todo():
    data = request.get_json()
    new_todo = Todo(
        title=data['title'],
        due_date=datetime.fromisoformat(data['due_date']) if 'due_date' in data else None,
        tags=','.join(data['tags']) if 'tags' in data else '',
        user_id=data.get('user_id')
    )
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({'message': 'Todo added'}), 201

@todo_bp.route('/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    t = Todo.query.get_or_404(todo_id)
    db.session.delete(t)
    db.session.commit()
    return jsonify({'message': 'Todo deleted'}), 200

@todo_bp.route('/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    t = Todo.query.get_or_404(todo_id)
    data = request.get_json()
    if 'title' in data:
        t.title = data['title']
    if 'due_date' in data:
        t.due_date = datetime.fromisoformat(data['due_date'])
    if 'tags' in data:
        t.tags = ','.join(data['tags'])
    if 'user_id' in data:
        t.user_id = data['user_id']
    db.session.commit()
    return jsonify({'message': 'Todo updated'}), 200

@user_bp.route('/', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data.get('email', ''))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added'}), 201

@user_bp.route('/', methods=['GET'])
def list_users():
    users = User.query.all()
    response = [{'id': u.id, 'username': u.username, 'email': u.email} for u in users]
    return jsonify(response), 200

