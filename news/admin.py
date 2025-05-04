from django.contrib import admin

from news.models import Redactor, Topic, Newspaper


@admin.register(Redactor)
class RedactorAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'years_of_experience', 'is_active')
    search_fields = ('username', 'first_name', 'last_name')


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'topic')
    search_fields = ('title', 'topic__name')
    list_filter = ('published_date', 'topic')
