from django.apps import AppConfig

from configs.app_settings import CONTEXT_APP_NAME


class ContextConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = CONTEXT_APP_NAME
