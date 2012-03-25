from pyramid.scaffolds import PyramidTemplate

class BunsenTemplate(PyramidTemplate):
    _template_dir = "pyramid_template"
    summary = "A Pyramid project setup with URL Dispatch, Jinja2, SQLAlchemy, WTForms and more."
