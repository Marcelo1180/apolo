# helloworld.py

from nameko.rpc import rpc

class GreetingService:
    name = 'greeting_service'

    @rpc
    def actualizar(self, name):
        return 'Hello, {}!'.format(name)
