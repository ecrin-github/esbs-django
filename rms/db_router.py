from configs.app_settings import RMS_APP_NAME
from configs.rms_db_settings import RMS_DB_KEY_NAME


class RmsDbRouter:
    route_app_labels = {RMS_APP_NAME}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return RMS_DB_KEY_NAME
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return RMS_DB_KEY_NAME
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
            return db == RMS_DB_KEY_NAME
        return None
