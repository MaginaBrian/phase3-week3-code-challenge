import pytest
from lib.models.magazine import Magazine
from lib.db.seed import seed_database

@pytest.fixture
def setup_db():
    seed_database()
    yield

def test_magazine_creation(setup_db):
    magazine = Magazine("Test Mag", "Test Category")
    magazine.save()
    assert magazine.id is not None
    assert magazine.name == "Test Mag"
    assert magazine.category == "Test Category"

def test_magazine_articles(setup_db):
    magazine = Magazine.find_by_id(1)
    articles = magazine.articles()
    assert len(articles) >= 1

def test_magazine_contributors(setup_db):
    magazine = Magazine.find_by_id(1)
    contributors = magazine.contributors()
    assert len(contributors) >= 1

def test_top_publisher(setup_db):
    top_mag = Magazine.top_publisher()
    assert top_mag is not None