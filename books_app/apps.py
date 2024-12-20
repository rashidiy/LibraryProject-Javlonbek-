from django.apps import AppConfig


class BooksAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'books_app'

    def ready(self):
        import books_app.signals