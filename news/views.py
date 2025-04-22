from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from news.models import Newspaper, Topic, Redactor


def index(request: HttpRequest) -> HttpResponse:
    num_newspaper = Newspaper.objects.count()
    num_redactor = Redactor.objects.count()
    num_topic = Topic.objects.count()
    context = {
        "num_redactor": num_redactor,
        "num_newspaper": num_newspaper,
        "num_topic": num_topic,
    }
    return render(request, "news/index.html", context=context)


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    template_name = "news/newspaper_list.html"
    queryset = Newspaper.objects.all()


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    template_name = "news/redactor-list.html"
    queryset = Redactor.objects.all()


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    template_name = "news/topic.html"
    queryset = Topic.objects.all()

