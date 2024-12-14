from app import create_app, db
from app.models import User, Todo
from datetime import datetime

app = create_app()

with app.app_context():
    db.create_all()

    # Hozzáadunk egy felhasználót
    user = User(id=1, username='testuser', email='testuser@example.com')
    db.session.add(user)

    # Hozzáadunk egy Todo elemet
    todo = Todo(
        title="Első Teendő",
        due_date=datetime.strptime("2024-12-31T23:59:59", "%Y-%m-%dT%H:%M:%S"),  # Konvertáljuk datetime objektummá
        tags="munka,fontos",
        user_id=1
    )
    db.session.add(todo)

    db.session.commit()
    print("Adatbázis feltöltve!")
