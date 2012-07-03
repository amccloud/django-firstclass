from BeautifulSoup import BeautifulSoup
from django.core.mail import get_connection
from django.core.mail.backends.base import BaseEmailBackend
from django.core.mail.message import EmailMultiAlternatives
from django.utils.html import strip_tags
from .settings import *
from .utils import call_or_format

class EmailBackend(BaseEmailBackend):
    def __init__(self, **kwargs):
        self._backend = get_connection(FIRSTCLASS_EMAIL_BACKEND, **kwargs)
        super(EmailBackend, self).__init__(**kwargs)

    def send_messages(self, email_messages):
        messages = []

        for original in email_messages:
            html_body = self.process_html(original.body)
            text_body = self.process_text(html_body)

            message = EmailMultiAlternatives(
                subject=original.subject,
                body=text_body,
                from_email=original.from_email,
                to=original.to,
                bcc=original.bcc,
                connection=original.connection,
                attachments=original.attachments,
                headers=original.extra_headers,
                cc=original.cc)

            message.attach_alternative(html_body, 'text/html')
            messages.append(message)

        return self._backend.send_messages(messages)

    def process_html(self, html):
        return html

    def process_text(self, html):
        soup = BeautifulSoup(html)

        for el in soup.findAll('a'):
            el.replaceWith(call_or_format(FIRSTCLASS_TEXT_ANCHOR,
                dict(el.attrs, text=el.text)))

        for el in soup.findAll('img'):
            el.replaceWith(call_or_format(FIRSTCLASS_TEXT_IMAGE,
                dict(el.attrs)))

        text = strip_tags(unicode(soup))

        return text
