from django.core.management.base import BaseCommand
from site_app.models import RecipeModel
from django.contrib.auth.models import User
from faker import Faker
import random

fake = Faker('ru_RU')


class Command(BaseCommand):
    help = 'Generate fake recipes.'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Количество рецептов для генерации')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')

        # Получаем случайных пользователей для связи с рецептами
        users = list(User.objects.all())
        if not users:
            self.stdout.write(self.style.ERROR('Нет доступных пользователей. Сначала создайте хотя бы одного.'))
            return

        for _ in range(count):
            recipe = RecipeModel(
                title=fake.sentence(nb_words=3),
                description=fake.text(max_nb_chars=300),
                cooking_steps="\n".join(fake.sentences(nb=10)),
                cooking_time=random.randint(10, 120),
                image='recipe/imgholder.png',
                author=random.choice(users)
            )
            recipe.save()

        self.stdout.write(self.style.SUCCESS(f'{count} рецептов успешно добавлено!'))
