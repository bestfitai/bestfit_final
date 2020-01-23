from django.apps import AppConfig


class OnlineQuizConfig(AppConfig):
    name = 'online_quiz'

    def ready(self):
        from online_quiz import signals