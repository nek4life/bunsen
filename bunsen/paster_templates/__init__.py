from paste.deploy.converters import asbool
from paste.script.templates import var
from paste.util.template import paste_script_template_renderer
from pyramid.paster import PyramidTemplate

class BunsenTemplate(PyramidTemplate):
    _template_dir = "pyramid_template"
    summary = "A Pyramid project setup with URL Dispatch, Jinja2, SQLAlchemy, WTForms and more."
    template_renderer = staticmethod(paste_script_template_renderer)
