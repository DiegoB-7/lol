import modules.db.modules as db
from datetime import datetime



def run():
    db.db_init()
    db.create_rol()


if __name__ =="__main__":
    run()



def create_user():
    key = Fernet.generate_key()
    fernet = Fernet(key)
    message = "hola"
    db.User(name="Diego Beltran",email="diego_beltran123@live.com",password=fernet.encrypt(message.encode()),rol="",date_created=datetime.now())
    #commit()