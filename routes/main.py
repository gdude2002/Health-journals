__author__ = 'Gareth Coles'

GET = "GET"
POST = "POST"

# from bottle import HTTPError, request
from bottle import mako_template as template
from bottle import route


class Routes(object):

    app = None

    def __init__(self, app, manager):
        self.app = app
        self.manager = manager

        route("/", [GET, POST], self.index)
        # route("/api", [GET, POST], self.api_root)
        # route("/api/", [GET, POST], self.api_root)
        # route("/login", GET, self.login)
        # route("/login", POST, self.login_post)
        # route("/login/", GET, self.login)
        # route("/login/", POST, self.login_post)
        # route("/register", GET, self.register)
        # route("/register", POST, self.register_post)
        # route("/register/", GET, self.register)
        # route("/register/", POST, self.register_post)

    def index(self):
        return template("templates/index.html")

    # def register(self):
    #     pass
    #
    # def register_post(self):
    #     username = request.POST.get('user', '')
    #     password = request.POST.get('pwd', '')
    #     if username and password:
    #         pass
    #     else:
    #         if username:
    #             pass  # No password
    #         else:
    #             pass  # No username
    #
    # def login(self):
    #     pass
    #
    # def login_post(self):
    #     username = request.POST.get('user', '')
    #     password = request.POST.get('pwd', '')
    #     if username and password:
    #         pass
    #     else:
    #         if username:
    #             return HTTPError(300, "/login?error=password")
    #         else:
    #             return HTTPError(300, "/login?error=username")
    #
    # def api_login(self):
    #     pass
    #     # username = request.POST.get('user', '')
    #     # password = request.POST.get('pwd', '')
    #
    # def api_root(self):
    #     raise HTTPError(403, "GTFO.")
