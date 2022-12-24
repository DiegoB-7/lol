from pony.orm import *
from decouple import config

DB_USERNAME = config('DB_USERNAME')
DB_HOST = config('DB_HOST')
DB_PASSWORD = config('DB_PASSWORD')
DB_NAME = config('DB_NAME')

db = Database()

db.bind(provider='mysql', host = DB_HOST, user = DB_USERNAME, passwd = DB_PASSWORD, db = DB_NAME)

class Person(db.Entity):
    name = Required(str)
    age = Required(int)
    cars = Set('Car')