from ..db.connection import get_connection

class Author:
    def __init__(self, name, id=None):
        self._id = id
        self._name = None
        self.name = name  # Use setter for validation

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string")
        self._name = value

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            if self._id is None:
                cursor.execute(
                    "INSERT INTO authors (name) VALUES (?) RETURNING id",
                    (self.name,)
                )
                self._id = cursor.fetchone()[0]
            else:
                cursor.execute(
                    "UPDATE authors SET name = ? WHERE id = ?",
                    (self.name, self._id)
                )
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        return cls(row['name'], row['id']) if row else None

    @classmethod
    def find_by_name(cls, name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE name = ?", (name,))
        row = cursor.fetchone()
        conn.close()
        return cls(row['name'], row['id']) if row else None

    def articles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (self._id,))
        articles = cursor.fetchall()
        conn.close()
        return [dict(row) for row in articles]

    def magazines(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.* FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self._id,))
        magazines = cursor.fetchall()
        conn.close()
        return [dict(row) for row in magazines]

    def add_article(self, magazine, title):
        from .article import Article
        article = Article(title, self, magazine)
        article.save()
        return article

    def topic_areas(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.category FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self._id,))
        categories = [row['category'] for row in cursor.fetchall()]
        conn.close()
        return categories