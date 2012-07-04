from django.contrib.sites.models import Site
from django.template.loader import render_to_string
from firstclass.models import Message

DOMAIN = Site.objects.get_current().domain

class ViewOnlineMiddleware(object):
    def process_message(self, message):
        saved = Message.objects.create(data={
            'subject': message.subject,
            'body': message.body,
            'from_email': message.from_email,
            'to': message.to,
            'bcc': message.bcc,
            'cc': message.cc,
            'headers': message.extra_headers,
        })

        message.body = render_to_string('firstclass/view_online_wrap.html', {
            'body': message.body,
            'subject': message.subject,
            'url': 'http://%s%s' % (DOMAIN, saved.get_absolute_url()),
        })

        return message
