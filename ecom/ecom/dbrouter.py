
class DBRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """

    cart_app_label = {"cart"}
    product_app_label = {"product"}
    category_app_label = {"category"}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.cart_app_label:
            return "mongo"
        elif model._meta.app_label in self.product_app_label or model._meta.app_label in self.category_app_label:
            return "default"
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.cart_app_label:
            return "mongo"
        elif model._meta.app_label in self.product_app_label or model._meta.app_label in self.category_app_label:
            return "default"
        return  None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        # """
        # if (
        #     obj1._meta.app_label in self.route_app_labels
        #     or obj2._meta.app_label in self.route_app_labels
        # ):
        #     return True
        if (obj1._meta.db_table in {"cart_items", "product"} and obj2._meta.db_table in {"cart_items", "product"}):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        if app_label == "cart":
            return db == "mongo"
        elif app_label in {"product", "category"}:
            return db == "default"
        return None