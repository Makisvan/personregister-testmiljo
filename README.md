# Personregister – Testmiljö (GDPR)

Detta projekt är en enkel Python-applikation som simulerar hur testdata
(namn och e-post) kan hanteras enligt GDPR.

Appen använder:
- Python
- sqlite3
- Docker
- Docker Compose
- CI/CD Github Actions

## Funktioner

- Skapa testpersoner
- Visa lagrade personer
- Anonymisera personuppgifter (GDPR)
- Radera personer (soft delete enligt GDPR)

## Kör utan Docker

```bash
python app.py

## Kör med Docker
docker compose up --build


## Stoppa containern:

docker compose down

## Databas

Applikationen använder sqlite3 och skapar automatiskt en databasfil:

users.db
