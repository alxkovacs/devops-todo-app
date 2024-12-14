# tests/test_api.py

import pytest
from app import create_app, db
from app.models import Todo, User

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():
        db.create_all()

        # Hozzáadunk egy tesztfelhasználót user_id=1 értékkel
        user = User(id=1, username='testuser', email='testuser@example.com')
        db.session.add(user)
        db.session.commit()

        yield app.test_client()

        db.session.remove()
        db.drop_all()

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory DB a tesztekhez

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()

def test_add_todo(client):
    response = client.post('/todos/', json={'title': 'Test Todo'})
    assert response.status_code == 201
    assert response.get_json()['message'] == 'Todo added'

def test_list_todos(client):
    client.post('/todos/', json={'title': 'Test Todo 2'})
    response = client.get('/todos/')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['title'] == 'Test Todo 2'



def test_create_todo_with_data(client):
    data = {
        "title": "Első Teendő",
        "due_date": "2024-12-31T23:59:59",
        "tags": ["munka", "fontos"],
        "user_id": 1
    }
    response = client.post('/todos/', json=data)
    assert response.status_code == 201
    assert response.get_json()['message'] == 'Todo added'