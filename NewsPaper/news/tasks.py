import datetime
import logging

from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives, mail_managers

from news.models import Post

logger = logging.getLogger(__name__)


@shared_task
def send_weekly_newsletter():
    last_week = datetime.datetime.now() - datetime.timedelta(weeks=1)

    posts = Post.objects.filter(created_at__gt=last_week)

    if posts.exists():
        text = '\n'.join([f'{p.author}: {p.title}' for p in posts])
        mail_managers("Новые статьи за неделю:", text)
    else:
        logger.info("Нет статей на отправку")


@shared_task
def after_add_post(pk):
    post = Post.objects.get(pk=pk)
    print(f'{post=}')
    emails = User.objects.filter(
        subscriptions__category__in=post.categories.all()
    ).values_list('email', flat=True)

    subject = f'Новый пост в категории {post.categories}'

    text_content = (
        f'Пост: {post.title}\n'
        f'Автор: {post.author}\n\n'
        f'Ссылка на пост: http://127.0.0.1:8000{post.get_absolute_url()}'
    )
    html_content = (
        f'Пост: {post.title}<br>'
        f'Автор: {post.author}<br><br>'
        f'<a href="http://127.0.0.1{post.get_absolute_url()}">'
        f'Ссылка на пост</a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
