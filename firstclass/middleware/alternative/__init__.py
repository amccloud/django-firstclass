from django.core.mail.message import EmailMultiAlternatives

class MultiAlternativesMiddleware(object):
    def process_message(self, message):
        return EmailMultiAlternatives(
            subject=message.subject,
            body=message.body,
            from_email=message.from_email,
            to=message.to,
            bcc=message.bcc,
            connection=message.connection,
            attachments=message.attachments,
            headers=message.extra_headers,
            cc=message.cc)
