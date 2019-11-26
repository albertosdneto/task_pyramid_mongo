from pyramid.security import Allow, Everyone, Authenticated


class TaskFactory(object):
    __acl__ = [(Allow, Everyone, 'view'),
               (Allow, Authenticated, 'create'),
               (Allow, Authenticated, 'edit'),
               (Allow, Authenticated, 'delete'), ]

    def __init__(self, request):
        pass
