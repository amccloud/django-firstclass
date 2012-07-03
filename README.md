# Django Firstclass
Firstclass is a Django email backend that automatically converts html emails to multi-part emails with a text fallback.

## Install
```bash
pip install django-firstclass
```

Add ``'firstclass'`` to ``INSTALLED_APPS`` and set `EMAIL_BACKEND` to ``'firstclass.backends.EmailBackend'``.

## Settings
### FIRSTCLASS_EMAIL_BACKEND
The email backend to send processed emails to.

Default: ``'django.core.mail.backends.smtp.EmailBackend'``

### FIRSTCLASS_TEXT_ANCHOR
How to format anchors converted to text. All attributes found on the element can be used for formatting.

Default: ``'%(text)s (%(href)s)'``

### FIRSTCLASS_TEXT_IMAGE
How to format images converted to text. All attributes found on the element can be used for formatting.

Default: ``firstclass.settings.image_to_text`` which is ``'%(title)s: %(src)s'``
