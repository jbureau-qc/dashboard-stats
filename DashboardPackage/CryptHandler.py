from cryptography.fernet import Fernet
from os.path import exists
import sys

def get_key():
    path = "~/Dashboard/dashboard-stats/DashboardPackage/key"    
    if (exists(path)):
       with open(path, "rb") as f:
          key = f.read()
    else:
       key = Fernet.generate_key()
       with open(path, "wb") as f:
          f.write(key)
    return key

def generate_crypted_with_key(password):
    message = password.encode()
    key = get_key()
    f = Fernet(key)
    encrypted = f.encrypt(message)
    print(str(encrypted))

if len(sys.argv) == 2:
    password = str(sys.argv[1]).replace("-p ", "")           
    generate_crypted_with_key(password)
else:    
    print("Missing argument")
    
