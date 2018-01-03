from __future__ import print_function
import configparser
import gettext
from fabric.api import env, settings


gettext.textdomain('hello')
gettext.bindtextdomain('hello', '/mo')
_ = gettext.gettext

config = configparser.ConfigParser()
config.read('config/config.ini')
PASSWORD = config['DEFAULT']['password']
FORWARD_AGENT = config['DEFAULT'].getboolean('forward_agent')
KEY_FILENAME = config['DEFAULT']['key_filename']

def apolo_out(func):
    def handle_error(*args, **kwargs):
        try:
            print(func(*args, **kwargs))
        except Exception as e:
            print(_('Ocurrio el siguiente error, {:}'.format(e)))
    return handle_error

def apolo_fabric(func):
    def handle_error(*args, **kwargs):
        env.password = PASSWORD
        # http://blog.desafiolatam.com/configurando-git-github-osx-linux/
        env.forward_agent = FORWARD_AGENT
        with settings(host_string='localhost', key_filename=KEY_FILENAME):
            # with settings(host_string='localhost'):
            return func(*args, **kwargs)
    return handle_error
