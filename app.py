import sqlite3
import os

DB_NAME = "users.db"


# --------- Databas ---------
def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            created_at TEXT NOT NULL,
            deleted_at TEXT
        )
    """)
    conn.commit()
    conn.close()


# --------- GDPR-funktioner ---------
def add_user():
    name = input("Ange namn: ")
    email = input("Ange e-post: ")

    conn = get_connection()
    conn.execute(
        "INSERT INTO users (name, email, created_at) VALUES (?, ?, datetime('now'))",
        (name, email)
    )
    conn.commit()
    conn.close()

    print("✅ Användare skapad")


def list_users():
    conn = get_connection()
    cursor = conn.execute(
        "SELECT id, name, email, created_at FROM users WHERE deleted_at IS NULL"
    )
    users = cursor.fetchall()
    conn.close()

    print("\n--- Användare ---")
    for user in users:
        print(f"{user[0]} | {user[1]} | {user[2]} | {user[3]}")


def anonymize_user():
    user_id = input("Ange användar-ID att anonymisera: ")

    conn = get_connection()
    conn.execute("""
        UPDATE users
        SET name = 'ANONYMIZED',
            email = 'anonymized@example.invalid'
        WHERE id = ?
    """, (user_id,))
    conn.commit()
    conn.close()

    print("✅ Användare anonymiserad (GDPR)")


def delete_user():
    user_id = input("Ange användar-ID att radera: ")

    conn = get_connection()
    conn.execute("""
        UPDATE users
        SET deleted_at = datetime('now')
        WHERE id = ?
    """, (user_id,))
    conn.commit()
    conn.close()

    print("✅ Användare raderad (GDPR)")

def reset_test_data():
    conn = get_connection()

    # Töm tabellen
    conn.execute("DELETE FROM users")

    # Lägg in testdata igen
    test_users = [
        ("Anna Test", "anna@test.se"),
        ("Bertil Test", "bertil@test.se"),
        ("Cecilia Test", "cecilia@test.se")
    ]

    for name, email in test_users:
        conn.execute(
            "INSERT INTO users (name, email, created_at) VALUES (?, ?, datetime('now'))",
            (name, email)
        )

    conn.commit()
    conn.close()

    print("✅ Testdata har återställts")



# --------- Meny ---------
def show_menu():
    print("\n=== GDPR Test Data System ===")
    print("1. Lägg till användare")
    print("2. Visa användare")
    print("3. Anonymisera användare")
    print("4. Radera användare")
    print("5. Återställ testdata")
    print("6. Avsluta")



def main():
    init_db()

    while True:
        show_menu()
        choice = input("Välj: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            list_users()
        elif choice == "3":
            anonymize_user()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            reset_test_data()
        elif choice == "6":
            print("Hejdå 👋")
            break
        else:
            print("❌ Ogiltigt val")


if __name__ == "__main__":
    main()
