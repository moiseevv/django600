from django.apps import AppConfig
from django.dispatch import Signal
from .utilities import send_activation_notification

user_registered = Signal()
# user_registered = Signal(providing_args=['instance'])

def user_register_dispatcher(sender, **kwargs):
    send_activation_notification(kwargs['instance'])

user_registered.connect(user_register_dispatcher)


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    verbose_name = 'Доска объявлений'
