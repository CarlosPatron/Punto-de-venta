from werkzeug.security import generate_password_hash

def encrypt_password(password):
    crypted_pass = generate_password_hash(password)
    print(len(crypted_pass))

encrypt_password('HolaMundo')