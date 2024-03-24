from django.apps import AppConfig


class BrainbusterappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'BrainBusterApp'

    def ready(self) -> None:
        from BrainBusterSite.create_score import create_user_score
