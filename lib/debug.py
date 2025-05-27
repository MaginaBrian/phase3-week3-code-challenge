
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.connection import get_connection

def debug():
    conn = get_connection()
    cursor = conn.cursor()
    
    
    cursor.execute("SELECT * FROM authors")
    print("Authors:", [dict(row) for row in cursor.fetchall()])
    
    cursor.execute("SELECT * FROM magazines")
    print("Magazines:", [dict(row) for row in cursor.fetchall()])
    
    cursor.execute("SELECT * FROM articles")
    print("Articles:", [dict(row) for row in cursor.fetchall()])
    
    conn.close()

if __name__ == "__main__":
    debug()