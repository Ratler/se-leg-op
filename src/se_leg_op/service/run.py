import logging

from .app import oidc_provider_init_app

name = 'oidc_provider'
app = oidc_provider_init_app(name)
logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    app.logger.info('Starting {} app...'.format(name))
    app.run()
