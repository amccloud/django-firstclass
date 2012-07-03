def call_or_format(func, attrs):
    if hasattr(func, '__call__'):
        return func(attrs)

    return func % attrs
