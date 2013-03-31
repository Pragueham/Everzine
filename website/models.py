from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class EditionManager(models.Manager):
    def live(self):
        return self.model.objects.filter(published=True)

class ArticleManager(models.Manager):
    def live(self):
        return self.model.objects.filter(published=True)


class Edition(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    title = models.CharField(max_length=255)
    number = models.IntegerField()
    slug = models.SlugField(max_length=255, blank=True, default='')
    published = models.BooleanField(default=True)
    objects = EditionManager()

    def __unicode__(self):
        return self.title


class Article(models.Model):
    CATEGORIES = (
        ('East', 'East'),
        ('West', 'West'),
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, default='')
    content = models.TextField()
    published = models.BooleanField(default=True)
    titleimage = models.ImageField(upload_to='photos')
    heroimage = models.ImageField(upload_to='photos')
    edition = models.ForeignKey('Edition')
    author = models.ForeignKey(User, related_name="articles")
    category = models.CharField(max_length=4, choices=CATEGORIES)
    objects = ArticleManager()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ("website:detail", (), {"slug": self.slug} )

class Credit(models.Model):
    role = models.CharField(max_length=1000)
    person = models.CharField(max_length=1000)
    article = models.ForeignKey('Article')

class Photo(models.Model):
    title = models.CharField(max_length=1000)
    photo = models.ImageField(upload_to='photos')
    article = models.ForeignKey('Article')
