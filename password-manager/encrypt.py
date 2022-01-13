from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    path = str(input("What path to generate key ?"))
    with open(f'{path}', 'wb') as mykey:
        mykey.write(key)

def encrypt(pathkey: str):
    with open(f'{pathkey}', 'rb') as mykey:
        key = mykey.read()
    f = Fernet(key)
    with open('C:/Users/rub75/OneDrive/Documents/Programmation/Python/BootcampPy2022/password-manager/data.json', 'rb') as orig_data:
        original = orig_data.read()
    encrypted = f.encrypt(original)
    with open('C:/Users/rub75/OneDrive/Documents/Programmation/Python/BootcampPy2022/password-manager/data.json', 'wb') as enc_file:
        enc_file.write(encrypted)
