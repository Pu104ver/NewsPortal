"""DISCLAIMER:
Запускал и проверял код командой
'exec(open('sf_exam/commands.py').read())'
войдя перед этим в shell.
Может вам тоже пригодится.
Попыток было много, поэтому пришлось отлаживать код.
Возможно, некоторые функции можно убрать, но мне как-то не хочется, времени 5 утра, а я все сижу..
нагоняю материал после сессии и перед сессией.
В общем, удачи в понимании!"""


from django.contrib.auth.models import User
from sf_exam.models import Author, Category, Post, Comment

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NewsPaper.settings")
django.setup()


def create_author_if_not_exists(user):
    """Отладочная функция, чтобы я не писал каждый раз уникального пользователя после обсёра исполнения кода до этого"""
    author_exists = Author.objects.filter(user=user).exists()

    if not author_exists:
        author = Author.objects.create(user=user, rating=0)
        return author

    return Author.objects.get(user=user)


def create_category_if_not_exists(name):
    """Отладочная функция"""
    category_exists = Category.objects.filter(name=name).exists()

    if not category_exists:
        category = create_category_if_not_exists(name=name)
        return category

    return Category.objects.get(name=name)


def create_unique_user(username_prefix):
    """Отладочная функция"""
    username = f'{username_prefix}_{User.objects.count()}'
    user = User.objects.create_user(username)

    return user


user1 = create_unique_user('user')
user2 = create_unique_user('user')

author1 = create_author_if_not_exists(user=user1)
author2 = create_author_if_not_exists(user=user2)

category1 = create_category_if_not_exists(name='Sports')
category2 = create_category_if_not_exists(name='Politics')
category3 = create_category_if_not_exists(name='Technology')
category4 = create_category_if_not_exists(name='Science')

post1 = Post.objects.create(author=author1, post_type='article', title='Article 1', content='Content 1', rating=0)
post2 = Post.objects.create(author=author2, post_type='article', title='Article 2', content='Content 2', rating=0)
post3 = Post.objects.create(author=author1, post_type='news', title='News 1', content='Content 3', rating=0)

post1.categories.add(category1, category2)
post2.categories.add(category3)
post3.categories.add(category4, category1)

comment1 = Comment.objects.create(post=post1, user=user1, text='Comment 1', rating=0)
comment2 = Comment.objects.create(post=post2, user=user2, text='Comment 2', rating=0)
comment3 = Comment.objects.create(post=post3, user=user1, text='Comment 3', rating=0)
comment4 = Comment.objects.create(post=post1, user=user2, text='Comment 4', rating=0)

post1.like()
post2.dislike()
post3.like()
post3.like()
post3.like()
post3.like()
post3.like()
post3.like()
post3.like()
post3.like()
comment1.like()
comment2.like()
comment3.dislike()
comment4.like()

author1.update_rating()
author2.update_rating()

best_user = Author.objects.order_by('-rating').first()
print(f"Best User: {best_user.user.username}, Rating: {best_user.rating}")

best_post = Post.objects.filter(post_type='article').order_by('-rating').first()
print(f"Best Article - Date: {best_post.created_at}, Author: {best_post.author.user.username}, "
      f"Rating: {best_post.rating}, Title: {best_post.title}, Preview: {best_post.preview()}")

for comment in Comment.objects.all():
    print(f"Date: {comment.created_at}, User: {comment.user.username}, Rating: {comment.rating}, Text: {comment.text}")
