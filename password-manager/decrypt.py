from cryptography.fernet import Fernet

def decrypting(pathkey: str):   
    with open(f'{pathkey}', 'rb') as mykey:
        key = mykey.read()
    f = Fernet(key)
    with open('C:/Users/rub75/OneDrive/Documents/Programmation/Python/BootcampPy2022/password-manager/data.txt', 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    decrypted = f.decrypt(encrypted)
    with open('C:/Users/rub75/OneDrive/Documents/Programmation/Python/BootcampPy2022/password-manager/data.txt', 'wb') as enc_file:
        enc_file.write(decrypted)
