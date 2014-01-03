
__author__ = 'Gareth Coles'

import logging
import sys
import yaml

import bottle

from beaker.middleware import SessionMiddleware
from cork import Cork
from cork.sqlalchemy_backend import SqlAlchemyBackend

from core.sql import Setup
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

db = config["database"]
db_url = "%s://%s:%s@%s/%s"\
         % (db["type"], db["username"], db["password"], db["address"],
            db["database"])

session_opts = {
    'cache.type': 'file',
    'cache.data_dir': 'cache/data',
    'cache.lock_dir': 'cache/lock',
    'session.type': 'ext:database',
    'session.url': db_url,
    'session.validate_key': True,
}

app = bottle.default_app()
sql_setup = Setup(app, db_url)

backend = SqlAlchemyBackend(db_url, "users", "roles", "pending_users")
cork = Cork(backend=backend, initialize=True)

routes_setup = Routes(app, cork)


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
