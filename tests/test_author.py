import pytest
from lib.models.author import Author

def test_author_has_name():
    author = Author(1, "Test Author")
    assert author.name == "Test Author"

def test_author_all_returns_list():
    authors = Author.all()
    assert isinstance(authors, list)
    assert all(isinstance(a, Author) for a in authors)

def test_author_articles_returns_articles():
    authors = Author.all()
    if authors:
        articles = authors[0].articles()
        assert isinstance(articles, list)