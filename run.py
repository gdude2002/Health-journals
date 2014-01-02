__author__ = 'Gareth Coles'

import logging
import sys
import yaml
from bottle import run, default_app, hook, request

from core.sql import Setup

logging.basicConfig(
    format="%(asctime)s | %(levelname)8s | %(message)s",
    datefmt="%d %b %Y - %H:%M:%S",
    level=(logging.DEBUG if "--debug" in sys.argv else logging.INFO))

logger = logging.getLogger("Main")

fh = open("config/config.yml", "r")
config = yaml.load(fh)
fh.close()

db = config["database"]
db_url = "%s://%s:%s@%s/%s"\
         % (db["type"], db["username"], db["password"], db["address"],
            db["database"])

app = default_app()


sql_setup = Setup(app, db_url)


@hook('before_request')
def log_all():
    ip = request.remote_addr
    logger.info("[%s] %s %s" % (ip, request.method, request.fullpath))

if __name__ == "__main__":
    run(app, server="cherrypy", host=config["server"]["host"],
        port=config["server"]["port"])
