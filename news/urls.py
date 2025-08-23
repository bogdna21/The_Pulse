from django.urls import path
from .views import (
    IndexView,
    AboutUsView,
    NewspaperListView,
    NewspaperDetailView,
    NewspaperDeleteView,
    NewspaperUpdateView,
    RedactorListView,
    RedactorDetailView,
    RedactorDeleteView,
    RedactorUpdateView,
    TopicListView,
    CustomPasswordResetView,
    CustomPasswordChangeView,
)

app_name = "news"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("about/", AboutUsView.as_view(), name="about-us"),

    path("newspapers/", NewspaperListView.as_view(), name="newspaper-list"),
    path("newspapers/<int:pk>/", NewspaperDetailView.as_view(), name="newspaper-detail"),
    path("newspapers/<int:pk>/delete/", NewspaperDeleteView.as_view(), name="newspaper-delete"),
    path("newspapers/<int:pk>/update/", NewspaperUpdateView.as_view(), name="newspaper-update"),

    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("redactors/<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail"),
    path("redactors/<int:pk>/delete/", RedactorDeleteView.as_view(), name="redactor-delete"),
    path("redactors/<int:pk>/update/", RedactorUpdateView.as_view(), name="redactor-update"),

    path("topics/", TopicListView.as_view(), name="topic-list"),

    path("password-reset/", CustomPasswordResetView.as_view(), name="custom_password_reset"),
    path("password-change/", CustomPasswordChangeView.as_view(), name="custom_password_change"),
]