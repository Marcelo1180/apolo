def art_deco(func):
    def handle_error(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            print('La funcion se ejecuto correctamente %s' % res)

        except Exception as e:
            descr = 'failed function because of {:}'.format(e)
            print(descr)
    return handle_error


@art_deco
def hola():
    print('2')
    return 'aaa'

@art_deco
def hola2():
    raise KeyError('oops')

rr = hola()
print(rr)
