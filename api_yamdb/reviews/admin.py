from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title

admin.site.register(Title)
admin.site.register(Genre)
admin.site.register(Category)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "review",
        "text",
        "author",
        "pub_date",
    )
    search_fields = ("review",)
    list_filter = ("review",)
    empty_value_display = "-пусто-"


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "text",
        "author",
        "score",
    )
    search_fields = ("pub_date",)
    list_filter = ("pub_date",)
    empty_value_display = "-пусто-"
