from django.apps import AppConfig

from configs.app_settings import RMS_APP_NAME


class RmsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = RMS_APP_NAME
