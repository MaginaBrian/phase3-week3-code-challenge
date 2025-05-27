# tests/test_author.py
import pytest
from lib.models.author import Author
from lib.db.connection import get_connection

@pytest.fixture
def setup_database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executescript("""
        DROP TABLE IF EXISTS authors;
        DROP TABLE IF EXISTS articles;
        DROP TABLE IF EXISTS magazines;
        CREATE TABLE authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255) NOT NULL
        );
        CREATE TABLE magazines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255) NOT NULL,
            category VARCHAR(255) NOT NULL
        );
        CREATE TABLE articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(255) NOT NULL,
            author_id INTEGER,
            magazine_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors(id),
            FOREIGN KEY (magazine_id) REFERENCES magazines(id)
        );
    """)
    conn.commit()
    conn.close()
    yield
    

def test_author_creation(setup_database):
    author = Author("Jane Doe")
    assert author.name == "Jane Doe"
    assert author.id is not None

def test_author_invalid_name(setup_database):
    with pytest.raises(ValueError):
        Author("")

def test_author_articles(setup_database):
    author = Author("Jane Doe")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Tech Today", "Technology"))
    magazine_id = cursor.lastrowid
    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", 
                  ("Test Article", author.id, magazine_id))
    conn.commit()
    conn.close()
    
    articles = author.articles()
    assert len(articles) == 1
    assert articles[0]['title'] == "Test Article"