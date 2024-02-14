from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Author, Category, Post, Comment, PostCategory


class CategoryAdminTranslation(TranslationAdmin):
    model = Category


class PostAdminTranslation(TranslationAdmin):
    model = Post


class PostAdmin(admin.ModelAdmin):
    list_display = 'author', 'post_type', 'get_categories', 'title'
    list_filter = 'categories', 'author',
    search_fields = ('title', 'categories__name')

    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])

    get_categories.short_description = 'Categories'


# Register your models here
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(PostCategory)
