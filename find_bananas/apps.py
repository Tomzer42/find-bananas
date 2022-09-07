from django.apps import AppConfig


class FindBananasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'find_bananas'


    def ready(self):
        from bananas_updater import updater
        updater.start()
