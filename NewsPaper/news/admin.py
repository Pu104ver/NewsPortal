from django.contrib import admin

from .models import Author, Category, Post, Comment, PostCategory


class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = 'author', 'post_type', 'get_categories', 'title'  # оставляем только имя и цену товара
    list_filter = 'categories', 'author',  # добавляем примитивные фильтры в нашу админку
    search_fields = ('title', 'categories__name')  # тут всё очень похоже на фильтры из запросов в базу

    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])

    get_categories.short_description = 'Categories'


# Register your models here
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(PostCategory)
