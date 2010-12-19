from pyramid.config import Configurator
from prices import root_factory

def main(global_config, **settings):
    """ This function returns a WSGI application.
    """

#    get_root = appmaker(engine)
    config = Configurator(settings=settings, root_factory=root_factory)
    zcml_file = settings.get('configure_zcml', 'configure.zcml')
    config.load_zcml(zcml_file)

    return config.make_wsgi_app()
