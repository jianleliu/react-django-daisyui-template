"""app config"""
from django.apps import AppConfig


class MyappConfig(AppConfig):
    """app config class. inherit default appconfig.

    Args:
        AppConfig (_type_): inherit default appconfig.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
