from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from .models import Post
from .tasks import after_add_post


@receiver(m2m_changed, sender=Post.categories.through)
def post_categories_changed(sender, instance, action, **kwargs):
    if action == 'post_add':
        # send_notification_to_subscribers(instance)
        after_add_post.delay(instance.pk)

#
# def send_notification_to_subscribers(post):
#     emails = User.objects.filter(
#         subscriptions__category__in=post.categories.all()
#     ).values_list('email', flat=True)
#
#     subject = f'Новый пост в категории {post.categories}'
#
#     text_content = (
#         f'Пост: {post.title}\n'
#         f'Автор: {post.author}\n\n'
#         f'Ссылка на пост: http://127.0.0.1:8000{post.get_absolute_url()}'
#     )
#     html_content = (
#         f'Пост: {post.title}<br>'
#         f'Автор: {post.author}<br><br>'
#         f'<a href="http://127.0.0.1{post.get_absolute_url()}">'
#         f'Ссылка на пост</a>'
#     )
#     for email in emails:
#         msg = EmailMultiAlternatives(subject, text_content, None, [email])
#         msg.attach_alternative(html_content, "text/html")
#         msg.send()
