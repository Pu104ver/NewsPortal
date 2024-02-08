from django.core.management.base import BaseCommand
from news.models import Post


class Command(BaseCommand):
    help = 'Удаляет все посты без категории'

    def handle(self, *args, **options):
        answer = input('Вы действительно хотите удалить все статьи без категории? yes/no\n')

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Отменено'))
            return

        try:
            # Получаем все статьи без категории
            uncategorized_posts = Post.objects.filter(categories__isnull=True)
            uncategorized_posts.delete()
            self.stdout.write(self.style.SUCCESS('Успешно удалены все статьи без категории'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Произошла ошибка: {str(e)}'))
