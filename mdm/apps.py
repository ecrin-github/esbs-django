from django.apps import AppConfig

from configs.app_settings import MDM_APP_NAME


class MdmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = MDM_APP_NAME
