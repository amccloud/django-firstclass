import sys, importlib

def get_cls_by_name(name, aliases={}, imp=None, package=None, sep='.', **kwargs):
    if not imp:
        imp = importlib.import_module

    if not isinstance(name, basestring):
        return name

    name = aliases.get(name) or name
    sep = ':' if ':' in name else sep

    module_name, _, cls_name = name.rpartition(sep)

    if not module_name and package:
        module_name = package

    try:
        module = imp(module_name, package=package, **kwargs)
    except ValueError, exc:
        raise ValueError("Couldn't import %r: %s" %
            (name, exc), sys.exc_info()[2])

    return getattr(module, cls_name)

def call_or_format(func, attrs):
    if hasattr(func, '__call__'):
        return func(attrs)

    return func % attrs
