from django.conf import settings

anchor_to_text = '%(text)s (%(href)s)'

def image_to_text(attrs):
    text = attrs.get('src')
    title = attrs.get('title', attrs.get('alt'), None)

    if title:
        text = '%s: %s' % (title, text)

    return text

FIRSTCLASS_EMAIL_BACKEND = getattr(settings, 'FIRSTCLASS_EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
FIRSTCLASS_TEXT_ANCHOR = getattr(settings, 'FIRSTCLASS_TEXT_ANCHOR', anchor_to_text)
FIRSTCLASS_TEXT_IMAGE = getattr(settings, 'FIRSTCLASS_TEXT_IMAGE', image_to_text)
