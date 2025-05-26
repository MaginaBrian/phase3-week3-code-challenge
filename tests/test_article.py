import pytest
from lib.models.article import Article
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.db.seed import seed_database

@pytest.fixture
def setup_db():
    seed_database()
    yield

def test_article_creation(setup_db):
    author = Author.find_by_id(1)
    magazine = Magazine.find_by_id(1)
    article = Article("Test Article", author, magazine)
    article.save()
    assert article.id is not None
    assert article.title == "Test Article"
    assert article.author.id == author.id
    assert article.magazine.id == magazine.id