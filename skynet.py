#!/usr/bin/fab -f
# class Contexto
from __future__ import print_function
import spacy
import sys


TAGS = {
    'acciones': ['crear', 'borrar', 'actualizar', ],
    'contexto': ['repositorio', 'proyecto']
}

action = {
    'layout': ['proyecto.repositorio.list()']
}

EXCLUDE_STOPWORDS = [
    'todo',
]


def str2command(phrase):
    nlp = spacy.load('es', disable=['parser', 'tagger', 'ner'])
    # print(nlp.pipe_names)
    doc = nlp(phrase)
    for token in doc:
        if (not token.is_stop) or (token.lemma_ in EXCLUDE_STOPWORDS):
            print(token.lemma_)


if __name__ == '__main__':
    str2command(' '.join(sys.argv[1:]))
