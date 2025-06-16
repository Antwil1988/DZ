from django.core.management.base import BaseCommand
from liba.models import Author, Book, Review
from django.utils import timezone
import random

class Command(BaseCommand):
    help = "Seed database with sample data"

    def handle(self, *args, **kwargs):
        Author.objects.all().delete()
        Book.objects.all().delete()
        Review.objects.all().delete()

        authors = [
            Author.objects.create(first_name="John", last_name="Doe", email="john.doe@example.com"),
            Author.objects.create(first_name="Alice", last_name="Brown", email="alice.brown@example.com"),
            Author.objects.create(first_name="Bob", last_name="Smith", email="bob.smith@example.com"),
            Author.objects.create(first_name="Eve", last_name="McDonald", email="eve.mcdonald@example.com"),
            Author.objects.create(first_name="John", last_name="McKenzie", email="john.mckenzie@example.com"),
        ]

        books = [
            Book.objects.create(title="Django Unleashed", author=authors[0], published_date=timezone.datetime(2023, 5, 10), price=499, discount=100, metadata={"genre": "tech", "tags": ["web", "bestseller"]}),
            Book.objects.create(title="Advanced Python Guide", author=authors[1], published_date=timezone.datetime(2024, 6, 15), price=1200, discount=200, metadata={"genre": "tech", "tags": ["advanced"]}),
            Book.objects.create(title="Python for Beginners", author=authors[2], published_date=timezone.datetime(2023, 1, 5), price=299, discount=0, metadata={"genre": "education", "tags": ["starter", "tutorial"]}),
            Book.objects.create(title="Professional Django Tutorial", author=authors[3], published_date=timezone.datetime(2023, 12, 25), price=750, discount=100, metadata={"genre": "tech", "tags": ["bestseller", "framework"]}),
            Book.objects.create(title="Fictional Story", author=authors[4], published_date=timezone.datetime(2024, 3, 30), price=450, discount=450, metadata={"genre": "fiction", "tags": ["novel"]}),
        ]

        for book in books:
            for i in range(3):
                Review.objects.create(book=book, rating=random.randint(1, 5), comment=(None if i % 2 == 0 else "Good book"), created_at=timezone.now().replace(second=0, microsecond=0))
