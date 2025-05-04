from django.urls import path, include
from .views import (
    index,
    NewspaperListView,
    TopicListView,
    RedactorListView,
    NewspaperDetailView,
    NewspaperDeleteView,
    NewspaperUpdateView, RedactorDetailView, RedactorDeleteView, RedactorUpdateView, about_us,
    custom_password_reset_request, custom_password_change_view
)


urlpatterns = [
    path("", index, name='index'),
    path("news/newpaper", NewspaperListView.as_view(), name="newspaper-list"),
    path("news/topic", TopicListView.as_view(), name="topic-list"),
    path("news/redactor/", RedactorListView.as_view(), name="redactor-list"),
    path("news/<int:pk>/detail/", NewspaperDetailView.as_view(), name="newspaper-detail"),
    path("news/<int:pk>/delete/", NewspaperDeleteView.as_view(), name="newspaper-delete"),
    path("news/<int:pk>/update/", NewspaperUpdateView.as_view(), name="newspaper-update"),
    path("news/redactor/<int:pk>/detail/", RedactorDetailView.as_view(), name="redactor-detail"),
    path("news/redactor/<int:pk>/detail/", RedactorDetailView.as_view(), name="redactor-detail"),
    path("news/redactor/<int:pk>/delete/", RedactorDeleteView.as_view(), name="redactor-delete"),
    path("news/redactor/<int:pk>/update/", RedactorUpdateView.as_view(), name="redactor-update"),
    path("news/about_us/", about_us, name="about-us"),
    path('password-reset/', custom_password_reset_request, name='custom_password_reset'),
    path('password-change/', custom_password_change_view, name='custom_password_change'),
]

app_name = "news"
