# Todo List API (Python + Flask)

Egyszerű és robusztus Todo List API Python és Flask segítségével, amely CRUD műveleteket, felhasználókezelést, címkézést, határidőket, CI/CD folyamatot, konténerizációt, tesztelést és monitorozást kínál. Ez a projekt bemutatja a teljes fejlesztési életciklust a beüzemeléstől a telepítésig és a monitorozásig.

## Tartalomjegyzék

- [Funkciók](#funkciók)
- [Használt Technológiák](#használt-technológiák)
- [Projekt Struktúrája](#projekt-struktúrája)
- [Telepítés és Beüzemelés](#telepítés-és-beüzemelés)
  - [Előfeltételek](#előfeltételek)
  - [A Repozitórium Klónozása](#a-repozitórium-klónozása)
  - [Függőségek Telepítése](#függőségek-telepítése)
  - [Környezeti Változók Beállítása](#környezeti-változók-beállítása)
  - [Az Alkalmazás Futattása](#az-alkalmazás-futattása)
- [API Végpontok](#api-végpontok)
  - [Todo Végpontok](#todo-végpontok)
  - [Felhasználó Végpontok](#felhasználó-végpontok)
- [Használati Példák](#használati-példák)
  - [Python Kód Példák](#python-kód-példák)
- [Tesztelés](#tesztelés)
- [CI/CD Folyamat](#cicd-folyamat)
- [Konténerizáció Dockerrel](#konténerizáció-dockerrel)
  - [Docker Image Építése](#docker-image-építése)
  - [Docker Konténer Futattása](#docker-konténer-futattása)
- [Telepítés](#telepítés)
- [Monitorozás](#monitorozás)
  - [Prometheus](#prometheus)
  - [Grafana](#grafana)

---

## Funkciók

- **CRUD Műveletek**: Todo-k létrehozása, lekérdezése, frissítése és törlése.
- **Felhasználókezelés**: Felhasználók hozzáadása és todo-k hozzárendelése felhasználókhoz.
- **Címkézés**: Todo-k címkézése a jobb szervezhetőség érdekében.
- **Határidők**: Határidők beállítása a todo-knak.
- **CI/CD Folyamat**: Automatizált tesztelés és telepítés GitHub Actions segítségével.
- **Konténerizáció**: Docker a konzisztens környezetek érdekében.
- **Tesztelés**: Átfogó tesztek pytest-tel.
- **Monitorozás**: Prometheus és Grafana a valós idejű monitorozáshoz.

## Használt Technológiák

- **Flask**: Python mikrokeretrendszer az API építéséhez.
- **SQLite**: Könnyűsúlyú relációs adatbázis.
- **SQLAlchemy**: ORM az adatbázis interakciókhoz.
- **pytest**: Tesztelési keretrendszer.
- **GitHub Actions**: CI/CD folyamat automatizálása.
- **Docker**: Konténerizációs platform.
- **Prometheus**: Monitorozási és figyelési eszköz.
- **Grafana**: Adatvizualizáció és monitorozás.

## Projekt Struktúrája

```plaintext
todo_app/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── database.py
│
├── tests/
│   └── test_api.py
│
├── prometheus_client_metrics/
│   └── prometheus.yml
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── Dockerfile
├── docker-compose.yaml
├── requirements.txt
└── README.md
```

---

## Telepítés és Beüzemelés

### Előfeltételek

- **Python 3.10+**
- **pip**
- **Git**
- **Docker** (opcionális, konténerizációhoz)
- **Docker Compose** (opcionális, monitorozási beállításhoz)

### A Repozitórium Klónozása

```bash
git clone https://github.com/felhasznalo/todo-app.git
cd todo-app
```

### Függőségek Telepítése

Ajánlott virtuális környezet használata:

```bash
python -m venv venv
source venv/bin/activate  # Windows esetén: venv\Scripts\activate
pip install -r requirements.txt
```

### Környezeti Változók Beállítása

Állítsd be a `FLASK_APP` környezeti változót:

Linux/MacOS:

```bash
export FLASK_APP=app
```

Windows:

```bash
set FLASK_APP=app
```

### Az Alkalmazás Futattása

Indítsd el a Flask fejlesztői szervert:

```bash
flask run
```

Az API elérhető a [http://localhost:5000](http://localhost:5000) címen.

---

## API Végpontok

### Todo Végpontok

#### Összes Todo Lekérdezése

- **Végpont**: `GET /todos/`
- **Válasz**:
  ```json
  [
    {
      "id": 1,
      "title": "Vásárolni",
      "due_date": "2024-12-31T12:00:00",
      "tags": "bevásárlás,urgent",
      "user_id": 1
    }
  ]
  ```json
  [
    {
      "id": 1,
      "title": "Vásárolni",
      "due_date": "2024-12-31T12:00:00",
      "tags": ["bevásárlás", "urgent"],
      "user_id": 1
    }
  ]
  ```

#### Új Todo Hozzáadása

- **Végpont**: `POST /todos/`
- **Kérés Törzse**:
  ```json
  {
    "title": "Új Feladat",
    "due_date": "2024-12-31T12:00:00",
    "tags": "munka,sürgős",
    "user_id": 1
  }
  ```
- **Válasz**:
  ```json
  {
    "message": "Todo added"
  }
  ```json
  {
    "title": "Új Feladat",
    "due_date": "2024-12-31T12:00:00",
    "tags": ["munka", "sürgős"],
    "user_id": 1
  }
  ```
- **Válasz**:
  ```json
  {
    "message": "Todo added"
  }
  ```

---

### Felhasználó Végpontok

#### Új Felhasználó Hozzáadása

- **Végpont**: `POST /users/`
- **Kérés Törzse**:
  ```json
  {
    "username": "Kovács János",
    "email": "janos.kovacs@example.com"
  }
  ```
- **Válasz**:
  ```json
  {
    "message": "User added"
  }
  ```json
  {
    "name": "Kovács János"
  }
  ```
- **Válasz**:
  ```json
  {
    "message": "User added"
  }
  ```

#### Összes Felhasználó Lekérdezése

- **Végpont**: `GET /users/`
- **Válasz**:
  ```json
  [
    {
      "id": 1,
      "username": "Kovács János",
      "email": "janos.kovacs@example.com"
    }
  ]
  ```json
  [
    {
      "id": 1,
      "name": "Kovács János"
    }
  ]
  ```

## Használati Példák

### Python Kód Példák

```python
import requests

# Első kérés: Felhasználó létrehozása
try:
    response1 = requests.post(
        "http://localhost:5000/users/",
        headers={"Content-Type": "application/json"},
        json={"username": "Kovács János", "email": "kovacs.janos@example.com"}
    )
    response1.raise_for_status()
    print(response1.json())
except requests.exceptions.RequestException as e:
    print(f"Hiba történt a felhasználó létrehozásakor: {e}")

# Második kérés: Teendő létrehozása
try:
    response2 = requests.post(
        "http://localhost:5000/todos/",
        headers={"Content-Type": "application/json"},
        json={
            "title": "Dokumentáció befejezése",
            "due_date": "2024-12-31T12:00:00",
            "tags": "dokumentáció,sürgős",  # Lista helyett vesszővel elválasztott szöveg
            "user_id": 1
        }
    )
    response2.raise_for_status()
    print(response2.json())
except requests.exceptions.RequestException as e:
    print(f"Hiba történt a teendő létrehozásakor: {e}")
```

---

## Tesztelés

A tesztek futtatása pytest-tel:

```bash
pytest
```

---

## CI/CD Folyamat

GitHub Actions-t használ az automatizált teszteléshez és telepítéshez. A konfiguráció a `.github/workflows/ci.yml` fájlban található.

---

## Konténerizáció Dockerrel

### Docker Image Építése

```bash
docker build -t felhasznalonev/todo-app:latest .
```

### Docker Konténer Futattása

```bash
docker run -p 5000:5000 felhasznalonev/todo-app:latest
```

---

## Monitorozás

### Prometheus

Prometheus gyűjti és tárolja a metrikákat. Konfiguráció: `prometheus_client_metrics/prometheus.yml`.

### Grafana

Grafana vizualizálja a Prometheus által gyűjtött adatokat. Elérhető a [http://localhost:3000](http://localhost:3000) címen.