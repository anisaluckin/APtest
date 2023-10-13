from django.contrib import admin
from django.apps import apps

for model_class in apps.get_app_config('audienceplatformtest').get_models():
    admin.site.register(model_class)
