import configparser

config = configparser.ConfigParser()
config.read('config.ini')

db_host = config.get('database','host')
port = config.get('database','port')

print(db_host,port)