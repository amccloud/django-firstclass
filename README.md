# Django Firstclass
Firstclass is a proxy email backend for Django that allows for global email transformations
such as automatically creating a plain text version of html emails or automatically creating
an online version of the email that can be read in browser.

## Install
```bash
pip install django-firstclass
```

 - Add ``'firstclass'`` to ``INSTALLED_APPS``
 - Add ``url(r'^email/', include('firstclass.urls'))`` to your urlconf.
 - Set ``EMAIL_BACKEND`` to ``'firstclass.backends.ProxyBackend'``
 - Syncdb

## Settings
### FIRSTCLASS_EMAIL_BACKEND
The email backend to send processed emails to after they've gone through the middleware.

##### Default
```python
FIRSTCLASS_EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
```

### FIRSTCLASS_MIDDLEWARE
Firstclass middleware works just like Django middleware. Firstclass applies middleware
in the order it's defined in ``FIRSTCLASS_MIDDLEWARE``, top-down. You can even create your
own middleware. See: [Custom Middleware](#custom-middleware)

##### Default
```python
FIRSTCLASS_MIDDLEWARE = (
    'firstclass.middleware.online.ViewOnlineMiddleware',
    'firstclass.middleware.alternative.MultiAlternativesMiddleware',
    'firstclass.middleware.text.PlainTextMiddleware',
)
```

## Available Middleware
### PlainTextMiddleware
``firstclass.middleware.text.PlainTextMiddleware``

#### Settings
##### FIRSTCLASS_PLAINTEXT_RULES
A dictionary of rules for converting html to plain text. Keys should be a qualified
selector for BeautifulSoup's ``findAll``. Values can either be a formatting string or
a function that accepts one argument, ``attrs``. All attributes found on the element
can be used for formatting or will be passed to your function in ``attrs``.

##### Default
```python
FIRSTCLASS_PLAINTEXT_RULES = {
    'a': '(%(text)s) %(href)s',
    'img': '%(title)s: %(src)s',
}
```

### MultiAlternativesMiddleware
``firstclass.middleware.alternative.MultiAlternativesMiddleware``

Coerces email to ``EmailMultiAlternatives`` so that a multiple versions of the
email can be added.

### ViewOnlineMiddleware
``firstclass.middleware.online.ViewOnlineMiddleware``

Saves all emails and adds a link to the email body so that they can be viewed online
in a web browser. Ideally this middleware should come before the ``PlainTextMiddlewware``
so that the link that is added is converted to plain text.

``ViewOnlineMiddleware`` uses the template ``firstclass/view_online_wrap.html`` to append
the link to the bottom of the email. You can override this by providing your own in your
templates directory.

## Custom Middleware
Defining custom middleware for Firstclass is simple. Middleware should be a single
Python class that defines ``process_message``.

### process_message
``process_message(self, message)``

``message`` is an [EmailMessage](https://docs.djangoproject.com/en/dev/topics/email/?from=olddocs/#emailmessage-objects)
or an ``EmailMessage`` like object. ``process_message`` should return ``message``
or ``None``. If it returns ``None`` the email will be dropped.

## Views
### view_message_online
``firstclass.views.view_message_online(request, key, template='firstclass/message.html')``

This view is used by the ``ViewOnlineMiddleware`` middleware. It's template is
located at ``firstclass/message.html``. You can override this by providing your own
in your templates directory. The render context contains ``message`` which is ``Message``
model instance.
