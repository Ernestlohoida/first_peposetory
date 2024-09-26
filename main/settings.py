import flask 
project = flask.Flask(
    import_name = "main",
    template_folder = "templates",
    static_url_path = "/main/"
)