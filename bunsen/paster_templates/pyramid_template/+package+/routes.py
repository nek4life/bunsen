""" A tidy module for specifying all of you routes configuration.
"""
def includeme(config):
    """ Add routes to the global config object.
    """
    config.add_route('home', '/')