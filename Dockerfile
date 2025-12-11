FROM python:3.11-slim

WORKDIR /app

# Kopiera ALLA filer till containern
COPY . .

# Standardkommando – kör appen om du bara startar containern
CMD ["python", "app.py"]




