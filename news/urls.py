from django.urls import path, include
from .views import index, NewspaperListView, TopicListView, RedactorListView

urlpatterns = [
    path("", index, name='index'),
    path("news/newpaper", NewspaperListView.as_view(), name="newspaper_list"),
    path("news/topic", TopicListView.as_view(), name="topic_list"),
    path("news/redactor/", RedactorListView.as_view(), name="redactor_list"),
    path("accounts/", include("django.contrib.auth.urls")),

]

app_name = "news"
