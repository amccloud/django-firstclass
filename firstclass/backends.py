from django.core.mail import get_connection
from django.core.mail.backends.base import BaseEmailBackend
from .settings import FIRSTCLASS_EMAIL_BACKEND, FIRSTCLASS_MIDDLEWARE
from .utils import get_cls_by_name

class ProxyBackend(BaseEmailBackend):
    def __init__(self, **kwargs):
        self._backend = get_connection(FIRSTCLASS_EMAIL_BACKEND, **kwargs)
        super(EmailBackend, self).__init__(**kwargs)

    def send_messages(self, email_messages):
        messages = []

        for message in email_messages:
            for path in FIRSTCLASS_MIDDLEWARE:
                middleware = get_cls_by_name(path)()
                message = middleware.process_message(message)

            if message:
                messages.append(message)

        return self._backend.send_messages(messages)

EmailBackend = ProxyBackend
