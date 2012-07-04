import random
from django.db import models
from django_extensions.db.fields.json import JSONField

class Message(models.Model):
    key = models.CharField(max_length=40, primary_key=True)
    data = JSONField()

    @models.permalink
    def get_absolute_url(self):
        return ('view_message_online', (), {
            'key': self.key,
        })

    def save(self, *args, **kwargs):
        if not self.key:
            while True:
                try:
                    self.key = '%04x' % random.getrandbits(40 * 4)
                    super(Message, self).save(*args, **kwargs)
                except:
                    continue
                else:
                    return

        super(Message, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"%s to %s" % (self.data['subject'], ', '.join(self.data['to']))
