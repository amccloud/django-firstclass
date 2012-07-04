from django.conf import settings

FIRSTCLASS_EMAIL_BACKEND = getattr(settings, 'FIRSTCLASS_EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
FIRSTCLASS_MIDDLEWARE = getattr(settings, 'FIRSTCLASS_MIDDLEWARE', (
    'firstclass.middleware.online.ViewOnlineMiddleware',
    'firstclass.middleware.alternative.MultiAlternativesMiddleware',
    'firstclass.middleware.text.PlainTextMiddleware',
))
