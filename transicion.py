

class Matter(object):
    pass

lump = Matter()

from transitions import Machine

machine = Machine(model=lump, states=['solid', 'liquid', 'gas', 'plasma'], initial='solid')

print(lump.state)
