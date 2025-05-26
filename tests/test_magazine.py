import pytest
from lib.models.magazine import Magazine
from lib.models.article import Article

def test_magazine_has_name_and_category():
    magazine = Magazine(1, "Tech Monthly", "Technology")
    assert magazine.name == "Tech Monthly"
    assert magazine.category == "Technology"

def test_magazine_all_returns_list():
    magazines = Magazine.all()
    assert isinstance(magazines, list)
    assert all(isinstance(m, Magazine) for m in magazines)

def test_magazine_articles_returns_articles():
    magazines = Magazine.all()
    if magazines:
        articles = magazines[0].articles()
        assert isinstance(articles, list)


def add_article(self, magazine, title):
    import sqlite3
    from lib.models.article import Article

    conn = sqlite3.connect('lib/db/database.db')
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)",
        (title, '', self.id, magazine.id)  # Empty content for now
    )

    conn.commit()
    article_id = cursor.lastrowid
    conn.close()

    return Article(id=article_id, title=title, content='', author_id=self.id, magazine_id=magazine.id)