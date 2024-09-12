from django.apps import AppConfig


class QuestionTwoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Question_two'


#connet the signals
from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'Question_two'

    def ready(self):
        import Question_two.signals
