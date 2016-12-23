'''Configuration script that reads config.json'''

import os
import sys
import json


class Config(object):
    '''configuration'''
    def __init__(self):
        config_file_name = 'config.json'
        scriptPath = os.path.realpath(__file__)
        scriptDir = os.path.dirname(scriptPath)
        self.config_file = os.path.join(scriptDir, config_file_name)
        with open(self.config_file, 'r') as config_file:
            self.config = json.load(config_file)
            self.config['key3'] = 'value3'
            self.config['httpsRoot'] = 'https://' + self.config['apiRoot'] \
                + '/' + self.config['version']
            self.config['currentDir'] = os.path.dirname(scriptPath)
            sys.path.append(self.config['currentDir'])

    def get(self):
        '''returns config'''
        return self.config

    def write_back(self):
        '''write it back to the file'''
        with open(self.config_file, 'w') as config_file:
            json.dump(self.config, config_file)

config = Config().get()
