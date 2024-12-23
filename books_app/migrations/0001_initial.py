# Generated by Django 5.1.3 on 2024-12-17 06:55

import books_app.validators
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('availability', models.CharField(choices=[('In stock', 'In stock'), ('Out of stock', 'Out of stock'), ('On sale', 'On sale'), ('New', 'New')], max_length=250)),
                ('format', models.CharField(choices=[('Standard', 'Standard'), ('Downloadable', 'Downloadable'), ('External', 'External')], max_length=250)),
                ('book_image', models.ImageField(blank=True, null=True, upload_to='images/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png', 'bmp', 'webp'])])),
                ('book_pdf', models.FileField(blank=True, null=True, upload_to='books_pdf/', validators=[books_app.validators.validate_file_type])),
                ('published_date', models.DateField(blank=True, null=True)),
                ('average_rating', models.DecimalField(decimal_places=1, default=0, max_digits=3)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books_app.author')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(blank=True, related_name='categories', to='books_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('rating', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='books_app.books')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
