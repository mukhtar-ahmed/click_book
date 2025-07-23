from passlib.context import CryptContext

hash_pwd = CryptContext(schemes=['bcrypt'],deprecated='auto')

def hash_password(user_password:str):
    return hash_pwd.hash(user_password)

def verify_hash_password(user_password:str, db_password:str):
    return hash_pwd.verify(user_password, db_password)