from django.urls import path, include
from .views import index, NewspaperListView, TopicListView, RedactorListView

urlpatterns = [
    path("", index, name='index'),
    path("news/newpaper", NewspaperListView.as_view(), name="newspaper-list"),
    path("news/topic", TopicListView.as_view(), name="topic-list"),
    path("news/redactor/", RedactorListView.as_view(), name="redactor-list"),


]

app_name = "news"
