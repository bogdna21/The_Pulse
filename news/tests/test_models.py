import pytest
from news.models import Newspaper, Topic, Redactor


@pytest.mark.django_db
def test_topic_str():
    topic = Topic.objects.create(name="Sports")
    assert str(topic) == "Sports"


@pytest.mark.django_db
def test_newspaper_str():
    topic = Topic.objects.create(name="Tech")
    newspaper = Newspaper.objects.create(title="AI News", content="test", topic=topic)
    assert "AI News" in str(newspaper)


@pytest.mark.django_db
def test_redactor_str():
    redactor = Redactor.objects.create_user(username="john", password="12345")
    assert str(redactor) == "john"
