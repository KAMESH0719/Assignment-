from django.apps import AppConfig


class QuestionOneConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Question_one'

#Connect to the signals
from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'Question_one'

    def ready(self):
        import Question_one.signals
