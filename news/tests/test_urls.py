from django.urls import reverse, resolve
from news import views


def test_index_url_resolves():
    url = reverse("news:index")
    assert resolve(url).func.view_class == views.IndexView


def test_about_us_url_resolves():
    url = reverse("news:about-us")
    assert resolve(url).func.view_class == views.AboutUsView


def test_newspaper_list_url_resolves():
    url = reverse("news:newspaper-list")
    assert resolve(url).func.view_class == views.NewspaperListView


def test_redactor_list_url_resolves():
    url = reverse("news:redactor-list")
    assert resolve(url).func.view_class == views.RedactorListView


def test_topic_list_url_resolves():
    url = reverse("news:topic-list")
    assert resolve(url).func.view_class == views.TopicListView
