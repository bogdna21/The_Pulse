from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import generic

from news.forms import TopicSearchForm
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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TopicListView, self).get_context_data(**kwargs)
        context["search_form"] = TopicSearchForm()
        return context

    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            return self.queryset.filter(name__icontains=name)
        return self.queryset
