from configs.app_settings import MDM_APP_NAME
from configs.mdm_db_settings import MDM_DB_KEY_NAME


class MdmDbRouter:
    route_app_labels = {MDM_APP_NAME}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return MDM_DB_KEY_NAME
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return MDM_DB_KEY_NAME
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
            return db == MDM_DB_KEY_NAME
        return None
