from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Edition(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    title = models.CharField(max_length=255)
    number = models.IntegerField()

    def __unicode__(self):
        return self.title


class Article(models.Model):
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

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Card, self).save(*args, **kwargs)

class Credit(models.Model):
    role = models.CharField(max_length=1000)
    person = models.CharField(max_length=1000)
    article = models.ForeignKey('Article')

class Photo(models.Model):
    title = models.CharField(max_length=1000)
    photo = models.ImageField(upload_to='photos')
    article = models.ForeignKey('Article')
