from django.apps import AppConfig

from configs.app_settings import GENERAL_APP_NAME


class GeneralConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = GENERAL_APP_NAME
