
__author__ = 'Gareth Coles'

import logging
import sys
import yaml

import bottle

from beaker.middleware import SessionMiddleware

from core.routes import Routes

bottle.TEMPLATE_PATH.append("templates")

logging.basicConfig(
    format="%(asctime)s | %(levelname)8s | %(message)s",
    datefmt="%d %b %Y - %H:%M:%S",
    level=(logging.DEBUG if "--debug" in sys.argv else logging.INFO))

logger = logging.getLogger()

fh = open("config/config.yml", "r")
config = yaml.load(fh)
fh.close()

session_opts = {
    'cache.type': 'file',
    'cache.data_dir': 'cache/data',
    'cache.lock_dir': 'cache/lock',
    'session.type': 'ext:database',
    'session.url': '',  # TODO
    'session.validate_key': True,
}

app = bottle.default_app()

routes_setup = Routes(app)


@bottle.hook('before_request')
def log_all():
    ip = bottle.request.remote_addr
    logger.info("[%s] %s %s" % (ip, bottle.request.method,
                                bottle.request.fullpath))

app = SessionMiddleware(app, session_opts)

application = app  # For uWSGI

if __name__ == "__main__":
    bottle.run(app, server="cherrypy", host=config["server"]["host"],
               port=config["server"]["port"])
