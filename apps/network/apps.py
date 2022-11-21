from django.apps import AppConfig


class NetworkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.network'

    def ready(self):
        import apps.network.signals  # noqa
