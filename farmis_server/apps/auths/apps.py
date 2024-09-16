from django.apps import AppConfig


class AuthsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.auths'
    label = 'auths'
    verbose_name = 'Authentication and Authorization'
    verbose_name_plural = 'Authentications and Authorizations'
