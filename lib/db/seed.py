from .connection import get_connection

def seed_database():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        
        cursor.execute("DELETE FROM articles")
        cursor.execute("DELETE FROM authors")
        cursor.execute("DELETE FROM magazines")

        
        authors = [
            ("Jane Doe",),
            ("John Smith",),
            ("Alice Johnson",)
        ]
        cursor.executemany("INSERT INTO authors (name) VALUES (?)", authors)

       
        magazines = [
            ("Tech Today", "Technology"),
            ("Health Weekly", "Health"),
            ("Science Monthly", "Science")
        ]
        cursor.executemany("INSERT INTO magazines (name, category) VALUES (?, ?)", magazines)

        articles = [
            ("Tech Trends 2025", 1, 1),
            ("AI Revolution", 1, 3),
            ("Healthy Living Tips", 2, 2),
            ("Quantum Breakthrough", 3, 3),
            ("Gadgets Galore", 1, 1)
        ]
        cursor.executemany("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", articles)

        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Error seeding database: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    seed_database()