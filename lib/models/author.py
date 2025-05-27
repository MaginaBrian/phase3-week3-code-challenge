
from lib.db.connection import get_connection

class Author:
    def __init__(self, name, id=None):
        self._id = id
        self._name = None
        self.name = name  
        if id is None:
            self.save()

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
            conn.execute("BEGIN TRANSACTION")
            if self._id is None:
                cursor.execute("INSERT INTO authors (name) VALUES (?)", (self._name,))
                self._id = cursor.lastrowid
            else:
                cursor.execute("UPDATE authors SET name = ? WHERE id = ?", (self._name, self._id))
            conn.execute("COMMIT")
        except Exception as e:
            conn.execute("ROLLBACK")
            raise Exception(f"Error saving author: {e}")
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
        conn = get_connection()
        cursor = conn.cursor()
        try:
            conn.execute("BEGIN TRANSACTION")
            cursor.execute(
                "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                (title, self._id, magazine.id)
            )
            conn.execute("COMMIT")
        except Exception as e:
            conn.execute("ROLLBACK")
            raise Exception(f"Error adding article: {e}")
        finally:
            conn.close()

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