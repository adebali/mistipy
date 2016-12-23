"""Taxonomy class"""

from .utils import session
from .config import config


class TaxonomyUnit(object):
    '''Taxonomy Unit class'''

    def __init__(self, id):
        self.id = id
        self.route = 'taxonomy'

    def info(self):
        '''Returns the response of the taxonomy unit'''
        path = config['httpsRoot'] + '/' + self.route + '/' + self.id
        response = session.get(path)
        return response.json()

    def parents(self):
        '''returns parents in a list'''
        path = config['httpsRoot'] + '/' + self.route + '/' \
            + '{}'.format(self.id) + '/parents'
        response = session.get(path)
        return response.json()

    def lineageString(self):
        lineage = []
        for node in self.parents():
            lineage.append(node['name'])
        return ';'.join(lineage)
