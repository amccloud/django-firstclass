from django.conf import settings

def anchor_to_text(attrs):
    text = attrs.get('href').strip()
    title = attrs.get('title', attrs.get('text')).strip()

    if text == title or not title:
        return text

    return '(%s) %s' % (title, text)

def image_to_text(attrs):
    text = attrs.get('src').strip()
    title = attrs.get('title', attrs.get('alt', None)).strip()

    if not title:
        return text

    return '%s: %s' % (title, text)

# Deprecated
FIRSTCLASS_TEXT_ANCHOR = getattr(settings, 'FIRSTCLASS_TEXT_ANCHOR', anchor_to_text)
FIRSTCLASS_TEXT_IMAGE = getattr(settings, 'FIRSTCLASS_TEXT_IMAGE', image_to_text)

FIRSTCLASS_PLAINTEXT_RULES = getattr(settings, 'FIRSTCLASS_PLAINTEXT_RULES', {
    'a': FIRSTCLASS_TEXT_ANCHOR,
    'img': FIRSTCLASS_TEXT_IMAGE,
})
