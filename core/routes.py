__author__ = 'Gareth Coles'

GET = "GET"
POST = "POST"

from bottle import HTTPError, request
from bottle import mako_template as template
from bottle import mako_view as view


class Routes(object):

    app = None
    cork = None

    def __init__(self, app, cork):
        self.app = app
        self.cork = cork
        app.route("/", [GET, POST], self.index)
        app.route("/api", [GET, POST], self.api_root)
        app.route("/api/", [GET, POST], self.api_root)
        app.route("/login", GET, self.login)
        app.route("/login", POST, self.login_post)
        app.route("/login/", GET, self.login)
        app.route("/login/", POST, self.login_post)
        app.route("/register", GET, self.register)
        app.route("/register", POST, self.register_post)
        app.route("/register/", GET, self.register)
        app.route("/register/", POST, self.register_post)

    @view("index")
    def index(self):
        return "Hello, world!"

    def register(self):
        pass

    def register_post(self):
        username = request.POST.get('user', '')
        password = request.POST.get('pwd', '')
        if username and password:
            self.cork.register(username, password, ' ')
        else:
            if username:
                pass  # No password
            else:
                pass  # No username

    def login(self):
        pass

    def login_post(self):
        username = request.POST.get('user', '')
        password = request.POST.get('pwd', '')
        if username and password:
            self.cork.login(username, password,
                            success_redirect='/?message=logged_in',
                            fail_redirect='/login?error=wrong')
        else:
            if username:
                return HTTPError(300, "/login?error=password")
            else:
                return HTTPError(300, "/login?error=username")

    def api_login(self):
        username = request.POST.get('user', '')
        password = request.POST.get('pwd', '')
        self.cork.login(username, password,
                        success_redirect='/',
                        fail_redirect='/login')

    def api_root(self):
        raise HTTPError(403, "GTFO.")
