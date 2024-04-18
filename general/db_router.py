from configs.app_settings import GENERAL_APP_NAME
from configs.general_db_settings import GENERAL_DB_KEY_NAME


class GeneralDbRouter:
    route_app_labels = {GENERAL_APP_NAME}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return GENERAL_DB_KEY_NAME
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return GENERAL_DB_KEY_NAME
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
                obj1._meta.app_label in self.route_app_labels or
                obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == GENERAL_DB_KEY_NAME
        return None
