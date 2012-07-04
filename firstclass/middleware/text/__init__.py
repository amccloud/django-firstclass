from BeautifulSoup import BeautifulSoup
from django.utils.html import strip_tags
from firstclass.utils import call_or_format
from .settings import FIRSTCLASS_PLAINTEXT_RULES

class PlainTextMiddleware(object):
    def process_message(self, message):
        if hasattr(message, 'attach_alternative'):
            message.attach_alternative(message.body, 'text/html')

        soup = BeautifulSoup(message.body)

        for selector, format in FIRSTCLASS_PLAINTEXT_RULES.iteritems():
            for el in soup.findAll(selector):
                text = call_or_format(format, dict(el.attrs, text=getattr(el, 'text')))
                el.replaceWith(text)

        text = strip_tags(unicode(soup))
        message.body = text

        return message
