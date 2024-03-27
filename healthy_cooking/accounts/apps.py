from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'healthy_cooking.accounts'

    def ready(self):
        import healthy_cooking.accounts.signals
