import logging
from pyramid.view import view_config

log = logging.getLogger(__name__)

@view_config(route_name='home', renderer='index.html')
def my_view(request):
    message = 'Oh Hai!'
    request.session.flash(message)
    return {'project':'{{package}}'}