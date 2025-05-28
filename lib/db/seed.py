
from lib.db.connection import get_connection

def seed_database():
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        conn.execute("BEGIN TRANSACTION")

        
        cursor.execute("INSERT INTO authors (name) VALUES (?)", ("Margret Ogolla",))
        cursor.execute("INSERT INTO authors (name) VALUES (?)", ("John Flanagan",))

    
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Tech Today", "Technology"))
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Health Weekly", "Health"))

        
        cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", 
                       ("AI Revolution", 1, 1))
        cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", 
                       ("Healthy Living", 1, 2))
        cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", 
                       ("Tech Trends", 2, 1))
        cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", 
                       ("Fitness Tips", 2, 2))

        conn.commit()
        print("✅ Database seeded successfully.")
        
    except Exception as e:
        conn.rollback()
        print(f"❌ Error seeding database: {e}")
        
    finally:
        conn.close()

if __name__ == "__main__":
    seed_database()
