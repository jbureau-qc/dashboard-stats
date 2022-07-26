from cryptography.fernet import Fernet
import sys

def generate_crypted_with_key(password):
    message = password.encode()
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted = f.encrypt(message)
    print(str(key) + ":" + str(encrypted))

if len(sys.argv) == 2:
    password = str(sys.argv[1]).replace("-p ", "")           
    generate_crypted_with_key(password)
else:    
    print("Missing argument")
    
