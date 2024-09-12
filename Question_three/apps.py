from django.apps import AppConfig


class QuestionThreeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Question_three'


# apps.py
from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'Question_three'

    def ready(self):
        import Question_three.signals
