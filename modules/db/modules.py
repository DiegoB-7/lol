import datetime
from pony.orm import *
from decouple import config
from cryptography.fernet import Fernet

DB_USERNAME = config('DB_USERNAME')
DB_HOST = config('DB_HOST')
DB_PASSWORD = config('DB_PASSWORD')
DB_NAME = config('DB_NAME')

db = Database()
db.bind(provider='mysql', host = DB_HOST, user = DB_USERNAME, passwd = DB_PASSWORD, db = DB_NAME,ssl={"verify_mode": None})

set_sql_debug(True)

class User(db.Entity):
    id = PrimaryKey(int,auto=True)
    name = Required(str,max_len=40)
    email = Required(str,max_len=20)
    password = Required(str,max_len=15)
    rol = Optional('Rol')
    date_created = Required(datetime.datetime,6)

class Rol(db.Entity):
    id = PrimaryKey(int,auto=True)
    name = Required(str,max_len=40)
    user =  Set(User)

class Champion(db.Entity):
    id = PrimaryKey(int,auto=True)
    name = Required(str,max_len=100)

@db_session
def create_rol():
    db.Rol(name="User")
    print("Rol Created Succesfully :)")

@db_session
def create_User():
    
    db.Rol(name="User")
    print("User Created Succesfully :)")

#First time created DB
def db_init():
    db.generate_mapping() 
    #db.create_tables()
    #db.drop_all_tables(with_all_data=True) 
    