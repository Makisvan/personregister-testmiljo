# 🛡️ GDPR Test Data System

Detta projekt är en enkel testmiljö för hantering av personuppgifter enligt GDPR.  
Systemet är byggt i Python med SQLite och körs i Docker för att simulera hur persondata kan behandlas säkert.

Projektet är avsett för utbildning och testning – ingen riktig persondata ska användas.

---

## 📦 Funktioner

Systemet simulerar vanliga GDPR-relaterade åtgärder:

✅ Skapa användare (namn + e-post)  
✅ Visa lagrade användare  
✅ Anonymisera användare  
✅ Radera användare (soft delete)  
✅ Återställa testdata  

---

## 🛠 Teknik

Projektet använder:

- Python 3.11  
- SQLite3  
- Docker  
- Docker Compose  
- GitHub Actions (CI)  

---

## 📁 Projektstruktur

personregister-testmiljo/
├── app.py
├── test_gdpr.py
├── Dockerfile
├── docker-compose.yml
├── users.db
├── .gitignore
└── .github/
└── workflows/
└── ci.yml

## 🚀 Starta systemet

### 1️⃣ Bygg och starta containern

```powershell
docker compose up --build -d
Containern hålls nu igång i bakgrunden, och din lokala kod speglas automatiskt via volymen.

2️⃣ Stoppa systemet
powershell
Kopiera kod
docker compose down
▶️ Använd systemet
När programmet startar visas denna meny:

=== GDPR Test Data System ===
1. Lägg till användare
2. Visa användare
3. Anonymisera användare
4. Radera användare
5. Återställ testdata
6. Avsluta
Exempel på flöde:

Välj 1 → Lägg till användare

Ange namn och e-post

Välj 2 → Visa användare

Välj 3 → Anonymisera användare

Välj 4 → Radera användare

Välj 5 → Återställ testdata

🧪 Köra tester
Kör en specifik testfil
powershell

Kopiera kod
docker exec -it gdpr-python-app python /app/test_gdpr.py

Kör alla tester i /app automatiskt
powershell

Kopiera kod
docker exec -it gdpr-python-app python -m unittest discover -s /app -p "test*.py"

Testerna använder en separat databas test_users.db och påverkar inte produktionsdatabasen.

🔐 GDPR-simulering
Detta system simulerar flera viktiga GDPR-principer:

GDPR-rättighet	Funktion i systemet
Rätt till tillgång	Visa användare
Rätt till radering	Radera användare
Rätt till anonymisering	Anonymisera användare
Rätt till dataminimering	Endast nödvändiga fält lagras
Soft delete	deleted_at används istället för hård radering

🔄 CI/CD
Projektet innehåller en enkel GitHub Actions workflow som automatiskt körs vid:

push

pull request

Den testar att Python-koden kan startas korrekt.

⚠️ Viktigt
Detta projekt ska endast användas för test.
Använd aldrig riktig persondata.

👤 Författare
Skapad som ett testprojekt för GDPR-koncept och DevOps-övning.
