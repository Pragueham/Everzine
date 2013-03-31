# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Article, Edition

class PublishedArticlesMixin(object):
    def get_queryset(self):
        return self.model.objects.live()

class ArticleListView(PublishedArticlesMixin, ListView):
    model = Article


class PublishedEditionMixin(object):
    def get_queryset(self):
        return self.model.objects.live()

class EditionListView(PublishedEditionMixin, ListView):
    model = Edition