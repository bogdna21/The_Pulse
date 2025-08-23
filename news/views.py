from datetime import datetime

from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View, generic

from news.forms import (
    TopicSearchForm,
    RedactorSearchForm,
    NewspaperSearchForm,
    EmailVerificationForm,
    SetNewPasswordForm,
)
from news.models import Newspaper, Topic, Redactor


class IndexView(View):
    def get(self, request, *args, **kwargs) -> HttpResponse:
        num_newspaper = Newspaper.objects.count()
        num_redactor = Redactor.objects.count()
        num_topic = Topic.objects.count()
        year = datetime.now().year
        context = {
            "num_redactor": num_redactor,
            "num_newspaper": num_newspaper,
            "num_topic": num_topic,
            "year": year,
        }
        return render(request, "news/index.html", context=context)


class AboutUsView(View):
    def get(self, request, *args, **kwargs) -> HttpResponse:
        return render(request, "news/about_us.html")


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    template_name = "news/newspaper_list.html"
    queryset = Newspaper.objects.all()
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = NewspaperSearchForm()
        return context

    def get_queryset(self):
        title = self.request.GET.get("title")
        if title:
            return self.queryset.filter(title__icontains=title)
        return self.queryset


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper
    template_name = "news/newspaper_detail.html"


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("news:newspaper-list")


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    fields = "__all__"
    success_url = reverse_lazy("news:newspaper-list")


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    template_name = "news/redactor-list.html"
    queryset = Redactor.objects.all()
    context_object_name = "redactor_list"
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = RedactorSearchForm()
        return context

    def get_queryset(self):
        username = self.request.GET.get("username")
        if username:
            return self.queryset.filter(username__icontains=username)
        return self.queryset


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor
    template_name = "news/redactor_detail.html"


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("news:redactor-list")


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    fields = "__all__"
    success_url = reverse_lazy("news:redactor-list")


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    template_name = "news/topic.html"
    queryset = Topic.objects.all()
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = TopicSearchForm()
        return context

    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            return self.queryset.filter(name__icontains=name)
        return self.queryset


class CustomPasswordResetView(View):
    def get(self, request, *args, **kwargs):
        form = EmailVerificationForm()
        return render(request, "account/password_reset.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = EmailVerificationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            request.session["reset_email"] = email
            return redirect("news:custom_password_change")
        return render(request, "account/password_reset.html", {"form": form})


class CustomPasswordChangeView(View):
    def get(self, request, *args, **kwargs):
        email = request.session.get("reset_email")
        if not email:
            return redirect("news:custom_password_reset")

        form = SetNewPasswordForm()
        return render(
            request,
            "account/password_change.html",
            {"form": form, "email": email},
        )

    def post(self, request, *args, **kwargs):
        email = request.session.get("reset_email")
        if not email:
            return redirect("news:custom_password_reset")

        user = Redactor.objects.filter(email=email).first()
        if not user:
            return redirect("news:custom_password_reset")

        form = SetNewPasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data["new_password1"]
            user.password = make_password(password)
            user.save()
            request.session.pop("reset_email", None)
            return redirect("account_login")

        return render(
            request,
            "account/password_change.html",
            {"form": form, "email": email},
        )
