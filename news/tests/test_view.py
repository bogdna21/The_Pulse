import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth import get_user_model

from news.models import Newspaper, Topic, Redactor


@pytest.mark.django_db
class TestViews:
    def setup_method(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="testuser", password="12345", email="test@example.com"
        )
        self.client.login(username="testuser", password="12345")

    def test_index_view(self):
        url = reverse("news:index")
        response = self.client.get(url)
        assert response.status_code == 200
        assert "num_newspaper" in response.context

    def test_about_us_view(self):
        url = reverse("news:about-us")
        response = self.client.get(url)
        assert response.status_code == 200

    def test_newspaper_list_search(self):
        Newspaper.objects.create(title="Breaking", content="content")
        url = reverse("news:newspaper-list")
        response = self.client.get(url, {"title": "Break"})
        assert response.status_code == 200
        assert "Breaking" in response.content.decode()

    def test_redactor_list_search(self):
        Redactor.objects.create_user(username="redactor1", password="12345")
        url = reverse("news:redactor-list")
        response = self.client.get(url, {"username": "red"})
        assert response.status_code == 200
        assert "redactor1" in response.content.decode()

    def test_topic_list_search(self):
        Topic.objects.create(name="Politics")
        url = reverse("news:topic-list")
        response = self.client.get(url, {"name": "Polit"})
        assert response.status_code == 200
        assert "Politics" in response.content.decode()

    def test_custom_password_reset_and_change(self):
        url = reverse("news:custom_password_reset")
        response = self.client.post(url, {"email": self.user.email})
        assert response.status_code == 302
        assert self.client.session["reset_email"] == self.user.email

        url_change = reverse("news:custom_password_change")
        response = self.client.post(url_change, {"new_password1": "newpass123", "new_password2": "newpass123"})
        assert response.status_code == 302