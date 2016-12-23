"""Genome class"""

from .utils import session, streamElements
from .config import config


class Genome(object):
    '''Genome class'''

    def __init__(self, version):
        self.version = version
        self.route = 'genomes'

    def info(self):
        '''Returns the response of the genome'''
        path = config['httpsRoot'] + '/' + self.route + '/' + self.version
        response = session.get(path)
        return response.json()

    def iterateGenes(self, elementLimit=float("inf"), elementStart=1):
        '''iterate genes of a genome'''
        path = config['httpsRoot'] + '/' + self.route + '/' \
            + self.version + '/genes?fields.Dseq=true'
        return streamElements(path, elementLimit, elementStart)


class Genomes(object):
    '''Genomes stream'''

    def __init__(self):
        self.route = 'genomes'
        self.page = 0
        self.genomesAvailable = True

    def iterate(self, elementLimit=float("inf"), elementStart=1):
        '''iterates genomes'''
        path = config['httpsRoot'] + '/' + self.route
        return streamElements(path, elementLimit, elementStart)

    # @staticmethod
    # def popular():
    # 	path = 'https://api.themoviedb.org/3/tv/popular'
    # 	response = session.get(path)
    # 	return response.json()
