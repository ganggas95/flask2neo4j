from py2neo import Graph
from flask import _app_ctx_stack


class Flask2Neo4J:
    current_app = None
    transaction = None

    def __init__(self, app=None):
        self.current_app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.current_app = app
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions["flask2neo4j"] = self
        self._begin()

    def teardown(self, exception):
        ctx = _app_ctx_stack.top
        if hasattr(ctx, 'flask2neo4j'):
            ctx.flask2neo4j = None

    @property
    def graph(self):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'flask2neo4j'):
                ctx.flask2neo = self._connect
            return ctx.flask2neo

    @property
    def _connect(self):
        return Graph(
            self.current_app.config["NEO4J_URI"],
            username=self.current_app.config["NEO4J_USERNAME"],
            password=self.current_app.config["NEO4J_PASSWORD"])

    def _begin(self):
        self._connect.begin
