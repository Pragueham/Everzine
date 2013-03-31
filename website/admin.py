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
    fields = ("published", "edition", "title", "slug", "titleimage", "content", "category", "author")
    inlines = [CreditsInline, PhotosInline]
    list_display = ["published", "title", "edition", "category", "updated_at"]
    list_display_links = ["title"]
    list_editable = ["published"]
    list_filter = ["published", "category", "edition", "updated_at"]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}


class EditionAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    fields = ("published", "title", "number", "slug")
    list_display = ["published", "title", "updated_at"]
    list_display_links = ["title"]
    list_editable = ["published"]
    list_filter = ["published", "updated_at"]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Edition, EditionAdmin)