#!/usr/bin/fab -f
# class Contexto
from __future__ import print_function
import sys


class Automata:
    def __init__(self, cadena):
        self.items = cadena.split('')

    def _recorrer(self, estado, letra):
        if estado == 0 and letra == 'a':
            return 0

        if estado == 1 and letra == 'b':
            return 1

        if estado == 1 and letra == 'a':
            return 1
        return 0

    def run(self):
        # https://es.wikipedia.org/wiki/Aut%C3%B3mata_con_pila
        print('hola')

if __name__ == '__main__':
    automata(' '.join(sys.argv[1:]))
