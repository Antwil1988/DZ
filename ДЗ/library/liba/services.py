from django.db.models import F, Q, Count, Avg, ExpressionWrapper, DecimalField
from django.utils.timezone import datetime
from .models import Author, Book, Review

# === Базовые фильтры ===
def get_authors_named_john():
    return Author.objects.filter(first_name='John')

def get_authors_not_doe():
    return Author.objects.exclude(last_name='Doe')

# === Числовые сравнения ===
def get_books_price_lt_500():
    return Book.objects.filter(price__lt=500)

def get_books_price_lte_300():
    return Book.objects.filter(price__lte=300)

def get_books_price_gt_1000():
    return Book.objects.filter(price__gt=1000)

def get_books_price_gte_750():
    return Book.objects.filter(price__gte=750)

# === Поиск текста ===
def get_books_with_django():
    return Book.objects.filter(title__icontains='django')

def get_books_with_python_case_insensitive():
    return Book.objects.filter(title__icontains='python')

def get_books_title_startswith_advanced():
    return Book.objects.filter(title__startswith='Advanced')

def get_books_title_startswith_pro_case_insensitive():
    return Book.objects.filter(title__istartswith='pro')

def get_books_title_endswith_guide():
    return Book.objects.filter(title__endswith='Guide')

def get_books_title_endswith_tutorial_case_insensitive():
    return Book.objects.filter(title__iendswith='tutorial')

# === Null ===
def get_reviews_with_no_comment():
    return Review.objects.filter(comment__isnull=True)

def get_reviews_with_comment():
    return Review.objects.filter(comment__isnull=False)

# === IN и Range ===
def get_authors_by_ids():
    return Author.objects.filter(id__in=[1, 3, 5])

def get_books_published_in_2023():
    return Book.objects.filter(published_date__year=2023)

# === Регулярки ===
def get_books_title_regex_python():
    return Book.objects.filter(title__regex=r'^Python')

def get_authors_lastname_startswith_mc():
    return Author.objects.filter(last_name__iregex=r'^Mc')

# === Дата и время ===
def get_books_published_in_2024():
    return Book.objects.filter(published_date__year=2024)

def get_books_published_in_june():
    return Book.objects.filter(published_date__month=6)

def get_reviews_on_day_11():
    return Review.objects.filter(created_at__day=11)

def get_books_published_on_week_23():
    return Book.objects.filter(published_date__week=23)

def get_reviews_on_tuesday():
    return Review.objects.filter(created_at__week_day=3)  # 1 - Sunday, 2 - Monday, 3 - Tuesday

def get_books_published_in_q2():
    return Book.objects.filter(published_date__quarter=2)

def get_reviews_on_exact_date(date):
    return Review.objects.filter(created_at__date=date)

def get_reviews_at_exact_time():
    return Review.objects.filter(created_at__time=datetime.strptime("15:30", "%H:%M").time())

def get_reviews_at_15_hour():
    return Review.objects.filter(created_at__hour=15)

def get_reviews_at_30_minute():
    return Review.objects.filter(created_at__minute=30)

def get_reviews_with_zero_seconds():
    return Review.objects.filter(created_at__second=0)

# === Связанные поля ===
def get_books_by_author_email():
    return Book.objects.filter(author__email='author@example.com')

def get_books_by_author_lastname_contains_smith():
    return Book.objects.filter(author__last_name__icontains='smith')

def get_authors_with_more_than_5_books():
    return Author.objects.annotate(book_count=Count('books')).filter(book_count__gt=5)

# === JSON поля ===
def get_books_with_genre_fiction():
    return Book.objects.filter(metadata__genre='fiction')

def get_books_with_bestseller_tag():
    return Book.objects.filter(metadata__tags__icontains='bestseller')

# === F и Q выражения ===
def get_books_price_equals_discount():
    return Book.objects.filter(price=F('discount'))

def get_books_price_gt_discount():
    return Book.objects.filter(price__gt=F('discount'))

def get_authors_alice_or_not_brown():
    return Author.objects.filter(Q(first_name='Alice') | ~Q(last_name='Brown'))

# === Аннотации ===
def get_author_book_counts():
    return Author.objects.annotate(book_count=Count('books'))

def get_books_average_rating():
    return Book.objects.annotate(avg_rating=Avg('reviews__rating'))

def get_books_final_price():
    return Book.objects.annotate(final_price=ExpressionWrapper(F('price') - F('discount'), output_field=DecimalField()))

# === select_related / prefetch_related ===
def get_books_with_authors_optimized():
    return Book.objects.select_related('author')

def get_authors_with_books_optimized():
    return Author.objects.prefetch_related('books')
