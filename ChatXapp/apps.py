from django.apps import AppConfig


class ChatxappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ChatXapp'

    def ready(self) -> None:
        import ChatXapp.signals