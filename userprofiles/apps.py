from django.apps import AppConfig
from django.urls import reverse_lazy


class UserProfilesConfig(AppConfig):
    name = 'userprofiles'
    app_label = 'userprofiles'

    def ready(self):
        from userprofiles import signals
