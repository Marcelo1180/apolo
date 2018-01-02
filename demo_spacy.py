#!/usr/bin/fab -f
# class Contexto
from __future__ import print_function
import gettext

gettext.textdomain('hello')
gettext.bindtextdomain('hello', '/mo')
_ = gettext.gettext

print(_('Hello'))
print(_('World'))


def apolo_out(func):
    def handle_error(*args, **kwargs):
        try:
            print(func(*args, **kwargs))
        except Exception as e:
            print(_('Ocurrio el siguiente error, {:}'.format(e)))
    return handle_error

def apolo_fabric(func):
    def handle_error(*args, **kwargs):
        env.password = '*****'
        # http://blog.desafiolatam.com/configurando-git-github-osx-linux/
        env.forward_agent = True
        # with settings(host_string='localhost', key_filename='~/.ssh/id_rsa.pub'):
        with settings(host_string='localhost'):
            return func(*args, **kwargs)
    return handle_error


import sys
import getpass
from fabric.api import run, env, task, settings, local, sudo
from fabric.context_managers import cd


class Git(object):
    # def __init__(self):
    #     env.hosts = ['localhost']
    # @task
    # def git_clone(self, , branch):
    @apolo_out
    @apolo_fabric
    def git_pull(self, branch=''):
        # run('ssh-add -L')
        run('git pull')
        return _('Actualizacion correcta')
        # env.user = 'marcelo'
        # with settings(host_string="Remote", user = "ubuntu", key_filename="/home/ubuntu/key.pem"):
        # with settings(host_string='localhost', key_filename='~/.ssh/id_rsa.pub'):
        # with settings(host_string='geo.gob.bo', user='emendoza', key_filename='agetic'):
            # env.hosts = ['marcelo@localhost:22']
            # env.password = getpass.getpass('remote sudo password:')
            # run('git pull')

    # @task
    # def git_pull(self, branch=''):
    #     if branch:
    #         env.user = 'marcelo'
    #         env.hosts = ['localhost']
    #         env.password = getpass.getpass('remote sudo password:')
    #         run('echo "hola mortales"')
    #         return _('Repositorio actualizado')
    #     else:
    #         return _('data')


class Repositorio(object):
    def __init__(self, host, code_dir, url_repo, branch):
        self.__host = host
        self.__code_dir = code_dir
        self.__url_repo = url_repo
        self.__branch = branch

    @property
    def host(self):
        return self.__host

    @property
    def code_dir(self):
        return self.__code_dir

    @property
    def url_repo(self):
        return self.__url_repo

    @property
    def branch(self):
        return self.__branch


class RepositorioActualizar(Repositorio):
    def __init__(self, host, path, url_repo, branch):
        Repositorio.__init__(self, host, path, url_repo, branch)

    def run(self):
        g = Git()
        g.git_pull('')


import spacy


tag_dict = {
    'acciones': ['crear', 'borrar', 'actualizar', ],
    'contexto': ['repositorio', 'proyecto']
}

action = {
    'layout': ['proyecto.repositorio.list()']
}

def str2command(phrase):
    nlp = spacy.load('es', disable=['parser', 'tagger', 'ner'])
    # Desabilitando componentes se aumenta la velocidad
    print(nlp.pipe_names)

    doc = nlp(phrase)
    for token in doc:
        print(token.lemma_)
    # print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
    #       token.shape_, token.is_alpha, token.is_stop)


res = RepositorioActualizar('127.0.0.1', '/tmp/prueba', 'git@github.com:Marcelo1180/prueba.git', 'master')
res.run()

# str2command(u'Jarvis, actualizar todos los repositorios hoteles')
# str2command(u'Jarvis, actualiza el repositorios hotel')
# str2command(u'Jarvis, listar los repositorios hotel')
# str2command(u'Jarvis, muestrame los repositorios hotel')
# str2command(u'Jarvis, muestrame el repositorio hotel')
# str2command(u'Jarvis, muestrame todos los repositorios hotel')
# str2command(u'Jarvis, inicializa el espacio de trabajo del proyecto vivienda')
# str2command(u'Jarvis, crea el espacio de trabajo del proyecto vivienda')
# str2command(u'Jarvis, instancia el espacio de trabajo del proyecto vivienda')
# str2command(u'Jarvis, abre el espacio de trabajo del proyecto vivienda')
# str2command(u'Jarvis, inicializa los espacio de trabajo de los proyecto vivienda')
# str2command(u'Jarvis, inicializa el layout en consola del proyecto vivienda')

# >>import nltk
# >>nltk.download()
# >>import nltk
# >>nltk.download('wordnet')
# >>import nltk
# >>nltk.download('averaged_perceptron_tagger')

# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# from nltk.tag import pos_tag
# from nltk.stem import WordNetLemmatizer
# from nltk.stem.lancaster import LancasterStemmer
# from nltk.stem import SnowballStemmer


# IDIOMA = 'spanish'
# text = 'Jarvis actualiza todos los repositorios'
# stop_words = set(stopwords.words(IDIOMA))
# snowball_stemmer = SnowballStemmer(IDIOMA)
# words = word_tokenize(text)

# print(pos_tag(words))

# new_sentence = []

# for word in words:
#     if word not in stop_words:
#         print('-->', snowball_stemmer.stem(word))
#         new_sentence.append(word)

# print(new_sentence)
