from ..db.connection import get_connection

class Article:
    def __init__(self, title, author, magazine, id=None):
        self._id = id
        self._title = None
        self._author = author
        self._magazine = magazine
        self.title = title

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Title must be a non-empty string")
        self._title = value

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?) RETURNING id",
                (self.title, self.author.id, self.magazine.id)
            )
            self._id = cursor.fetchone()[0]
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()

    @classmethod
    def find_by_id(cls, id):
        from .author import Author
        from .magazine import Magazine
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            author = Author.find_by_id(row['author_id'])
            magazine = Magazine.find_by_id(row['magazine_id'])
            return cls(row['title'], author, magazine, row['id'])
        return None