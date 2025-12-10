import unittest
import sqlite3
import os
import app

class TestAnonymization(unittest.TestCase):

    def setUp(self):
        # Använd en separat testdatabas
        app.DB_NAME = "test_users.db"

        # Ta bort gammal testdatabas
        if os.path.exists(app.DB_NAME):
            os.remove(app.DB_NAME)

        # Skapa tabellen
        app.init_db()

        # Lägg till en testanvändare
        app.add_user("Test Person", "test@test.se")

    def test_anonymize_user(self):
        # Kör DIN anonymiseringsfunktion
        app.anonymize_user("1")

        # Läs direkt från databasen
        conn = sqlite3.connect(app.DB_NAME)
        cursor = conn.execute("SELECT name, email FROM users WHERE id = 1")
        user = cursor.fetchone()
        conn.close()

        # Kontrollera att datan är anonymiserad
        self.assertEqual(user[0], "ANONYMIZED")
        self.assertEqual(user[1], "anonymized@example.invalid")

if __name__ == "__main__":
    unittest.main()
