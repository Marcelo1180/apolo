import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')

print(config['repositorio'].getboolean('forward_agent'))
print(config.sections())
