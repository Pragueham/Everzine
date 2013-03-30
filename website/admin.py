from django.contrib import admin
from .models import Edition, Article, Credit, Photo


class CreditsInline(admin.TabularInline):
    model = Credit
    extra = 3

class PhotosInline(admin.TabularInline):
    model = Photo
    extra = 3

class ArticleAdmin(admin.ModelAdmin):
    # Show thumbnail in admin
    date_hierarchy = "created_at"
    fields = ("published", "title", "slug", "titleimage", "content", "author")
    inlines = [CreditsInline, PhotosInline]
    list_display = ["published", "titleimage", "title", "updated_at"]
    list_display_links = ["title"]
    list_editable = ["published"]
    list_filter = ["published", "updated_at"]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}



admin.site.register(Article, ArticleAdmin)