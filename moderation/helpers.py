from .register import RegistrationError


def automoderate(instance, user):
    '''
    Auto moderates given model instance on user. Returns moderation status:
    0 - Rejected
    1 - Approved
    '''
    try:
        status = instance.moderated_object.automoderate(user)
    except AttributeError:
        msg = "%s has been registered with Moderation." % instance.__class__
        raise RegistrationError(msg)

    return status


def import_moderator(app):
    '''
    Import moderator module and register all models it contains with moderation
    '''
    from importlib import import_module
    from importlib.util import find_spec

    try:
        import_module(app)
    except ImportError:
        return None

    spec = find_spec("%s.moderator" % app)
    if spec is None:
        return None

    module = import_module("%s.moderator" % app)

    return module
