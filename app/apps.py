from django.apps import AppConfig
from .signals import my_signal
import threading

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        # Connect the signal to the handler
        my_signal.connect(my_signal_handler)


def my_signal_handler(sender, **kwargs):
    print(f"Signal handler running in thread: {threading.current_thread().name}")

