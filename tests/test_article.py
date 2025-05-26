import pytest
from lib.models.article import Article
from lib.models.author import Author
from lib.models.magazine import Magazine

def test_article_has_title_and_content():
    article = Article(1, "Sample Title", "Sample Content", 1, 1)
    assert article.title == "Sample Title"
    assert article.content == "Sample Content"

def test_article_all_returns_list():
    articles = Article.all()
    assert isinstance(articles, list)
    assert all(isinstance(a, Article) for a in articles)

def test_article_relations():
    articles = Article.all()
    if articles:
        article = articles[0]
        assert article.author() is not None
        assert article.magazine() is not None