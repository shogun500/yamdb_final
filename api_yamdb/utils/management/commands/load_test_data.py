import os
from csv import DictReader

from comments.models import Comments
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from reviews.models import Review
from titles.models import Categories, Genres, Title

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        data_folder = os.path.join(
            settings.STATICFILES_DIRS[0], 'data'
        )

        for row in DictReader(
            open(f'{data_folder}/users.csv', encoding='utf-8')
        ):
            user = User(
                id=row['id'],
                username=row['username'],
                email=row['email'],
                bio=row['bio'],
                first_name=row['first_name'],
                last_name=row['last_name']
            )
            user.save()

        for row in DictReader(open(
            f'{data_folder}/genre.csv', encoding='utf-8')
        ):
            genre = Genres(
                id=row['id'],
                name=row['name'],
                slug=row['slug']
            )
            genre.save()

        for row in DictReader(open(
            f'{data_folder}/category.csv', encoding='utf-8')
        ):
            category = Categories(
                id=row['id'],
                name=row['name'],
                slug=row['slug']
            )
            category.save()

        for row in DictReader(open(
            f'{data_folder}/titles.csv', encoding='utf-8')
        ):
            title = Title(
                id=row['id'],
                name=row['name'],
                year=row['year'],
                category=Categories.objects.get(pk=row['category'])
            )
            title.save()

        for row in DictReader(open(
            f'{data_folder}/genre_title.csv', encoding='utf-8')
        ):
            title = Title.objects.get(pk=row['title_id'])
            title.genre.add(row['genre_id'])
            title.save()

        for row in DictReader(open(
            f'{data_folder}/review.csv', encoding='utf-8')
        ):
            review = Review(
                id=row['id'],
                title=Title.objects.get(pk=row['title_id']),
                text=row['text'],
                author=User.objects.get(pk=row['author']),
                score=row['score'],
                pub_date=row['pub_date']
            )
            review.save()

        for row in DictReader(open(
            f'{data_folder}/comments.csv', encoding='utf-8')
        ):
            comment = Comments(
                id=row['id'],
                review=Review.objects.get(pk=row['review_id']),
                text=row['text'],
                author=User.objects.get(pk=row['author']),
                pub_date=row['pub_date']
            )
            comment.save()
