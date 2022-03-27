from django.apps import AppConfig


class NewmovieConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newmovie'

    def ready(self):
        import newmovie.signals