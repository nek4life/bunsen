import os
from pyramid.httpexceptions import HTTPNotFound
from pyramid.response import Response
from pyramid.settings import asbool

def includeme(config):
    settings = config.registry.settings
    # Exceptions
    config.add_view(notfound_view, renderer='404.html', context=HTTPNotFound)
    
    if asbool(settings.get('custom_internal_server_error', 'false')):
        config.add_view(internal_error_view, renderer='500.html',
                        context=Exception)
    # Assets
    config.add_view(favicon_view, 'favicon.ico')
    config.add_view(crossdomain_view, 'crossdomain.xml')
    config.add_view(robots_view, 'robots.txt')
    config.add_view(humans_view, 'humans.txt')

# Exception Views
def notfound_view(request):
    request.response.status_int = 404
    current_url = request.application_url + request.path
    return {"current_url": current_url}

def internal_error_view(request):
    request.response.status_int = 500
    return {}

def _get_asset_response(asset_name, content_type):
    here = os.path.dirname(
           os.path.dirname(os.path.realpath(__file__)))
    asset = open(os.path.join(here, 'static', asset_name))
    return Response(content_type=content_type, app_iter=asset)

# Root-Relative Asset Views
def favicon_view(request):
    return _get_asset_response('favicon.ico', 'image/x-icon')

def crossdomain_view(request):
    return _get_asset_response('crossdomain.xml', 'text/xml')

def robots_view(request):
    return _get_asset_response('robots.txt', 'text/plain')

def humans_view(request):
    return _get_asset_response('humans.txt', 'text/plain')

