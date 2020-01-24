from django.apps import AppConfig


class OnlineQuizConfig(AppConfig):
    name = 'online_quiz'

    def ready(self):
        import online_quiz.signals