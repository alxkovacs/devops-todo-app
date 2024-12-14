# Dockerfile

FROM python:3.10-slim

# Munkakönyvtár létrehozása
WORKDIR /app

# Függőségek másolása
COPY requirements.txt .

# Függőségek telepítése
RUN pip install --no-cache-dir -r requirements.txt

# Alkalmazás kódjának másolása
COPY . .

# Környezeti változók beállítása
ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Port kinyitása
EXPOSE 5000

# Alkalmazás indítása
CMD ["flask", "run"]
