import pytest
from lib.models.author import Author
from lib.db.seed import seed_database
from lib.db.connection import get_connection

@pytest.fixture
def setup_db():
    seed_database()
    yield
    

def test_author_creation(setup_db):
    author = Author("Test Author")
    author.save()
    assert author.id is not None
    assert author.name == "Test Author"

def test_author_articles(setup_db):
    author = Author.find_by_id(1)
    articles = author.articles()
    assert len(articles) >= 1
    assert articles[0]['author_id'] == 1

def test_author_magazines(setup_db):
    author = Author.find_by_id(1)
    magazines = author.magazines()
    assert len(magazines) >= 1

def test_author_topic_areas(setup_db):
    author = Author.find_by_id(1)
    categories = author.topic_areas()
    assert len(categories) >= 1