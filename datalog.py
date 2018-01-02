from pyDatalog import pyDatalog
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey


engine = create_engine('sqlite:///:memory:', echo=False)

Session = sessionmaker(bind=engine)
session = Session()
Base.session = session
# Base = declarative_base(cls=pyDatalog.Mixin, metaclass=pyDatalog.sqlMetaMixin)

# from sqlalchemy import Column, Integer, String, ForeignKey

class Repositorio(Base):
    __tablename__ = 'repositorio'
    name = Column(String, primary_key=True)
    proyecto = Column(String)
    ruta = Column(String)

# now create the table
Base.metadata.create_all(engine)


# class Repositorio(pyDatalog.Mixin):
#     def __init__(self, name, proyecto, ruta):
#         super(Repositorio, self).__init__()
#         self.name = name
#         self.proyecto = proyecto
#         self.ruta = ruta

#     def __repr__(self):
#         return self.ruta


# pyDatalog.create_terms('X,Y,Z')
ja = Repositorio('asamblea:frontend', 'asamblea', 'http://ruta/front')
jc = Repositorio('asamblea:backend', 'asamblea', 'http://ruta/back')
pyDatalog.create_terms('X,Y')


print(Repositorio.proyecto[X]=='asamblea')
# print(X.v())

Repositorio.indirect_manager(X,Y) <= (Repositorio.proyecto[X]==Y) & (Y != None)

print(Repositorio.indirect_manager(X,Y))
# repositorio = ""
# pyDatalog.create_terms('X,Y,repositorio')
# repositorio['asamblea:frontend'] = 'http://url/frontend'
# repositorio['asamblea:backend'] = 'http://url/frontend'

# print(repositorio[X]==Y)


