from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
from django.db import models
from .validators import validate_file_type
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name

class Books(models.Model):
    class Availability(models.TextChoices):
        in_stock = 'In stock', 'In stock'
        out_of_stock = 'Out of stock', 'Out of stock'
        on_sale = 'On sale', 'On sale'
        new = 'New', 'New'
    class Format(models.TextChoices):
        standard = 'Standard', 'Standard'
        downloadable = 'Downloadable', 'Downloadable'
        external = 'External', 'External'

    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ManyToManyField(Category, related_name='books', blank=True)
    availability = models.CharField(max_length=250,choices=Availability.choices)
    format = models.CharField(max_length=250, choices=Format.choices)
    book_image = models.ImageField(upload_to='images/',
                                   validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'bmp', 'webp'])], null=True, blank=True)
    book_pdf = models.FileField(upload_to='books_pdf/',
                                validators=[validate_file_type], null=True, blank=True)
    published_date = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')

    @property
    def average_rating(self):
        reviews = self.reviews_set.all()
        if reviews.exists():
            return round(sum(review.rating for review in reviews) / reviews.count(), 1)
        return 0

    def __str__(self):
        return self.title


class Reviews(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user}-{self.book}"

