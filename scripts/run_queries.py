from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.db.connection import get_connection

def run_example_queries():
    conn = get_connection()
    cursor = conn.cursor()

    
    cursor.execute("""
        SELECT a.name, COUNT(art.id) as article_count
        FROM authors a
        JOIN articles art ON a.id = art.author_id
        GROUP BY a.id, a.name
        ORDER BY article_count DESC
        LIMIT 1
    """)
    top_author = cursor.fetchone()
    print(f"Top author: {top_author['name']} with {top_author['article_count']} articles")

    
    cursor.execute("""
        SELECT m.name, COUNT(DISTINCT art.author_id) as author_count
        FROM magazines m
        JOIN articles art ON m.id = art.magazine_id
        GROUP BY m.id, m.name
        HAVING author_count >= 2
    """)
    diverse_magazines = cursor.fetchall()
    print("Magazines with at least 2 different authors:")
    for mag in diverse_magazines:
        print(f"- {mag['name']}: {mag['author_count']} authors")

    conn.close()

if __name__ == "__main__":
    run_example_queries()