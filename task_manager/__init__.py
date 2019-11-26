from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator
from pymongo import MongoClient
from urllib.parse import urlparse


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    authentication_policy = AuthTktAuthenticationPolicy('somesecret')
    authorization_policy = ACLAuthorizationPolicy()

    with Configurator(settings=settings, authentication_policy=authentication_policy,
                      authorization_policy=authorization_policy) as config:
        db_url = urlparse(settings['mongo_uri'])
        config.registry.db = MongoClient(
            host=db_url.hostname,
            port=db_url.port,
        )

        def add_db(request):
            db = config.registry.db[db_url.path[1:]]
            if db_url.username and db_url.password:
                db.authenticate(db_url.username, db_url.password)
            return db

        config.add_request_method(add_db, 'db', reify=True)

        config.include('pyramid_jinja2')
        config.include('.routes')
        config.scan()
    return config.make_wsgi_app()
