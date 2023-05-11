from werkzeug.security import generate_password_hash, check_password_hash

password = 'Pa55word'
crypted_pass = generate_password_hash(password)

print(crypted_pass)
print(check_password_hash(crypted_pass, password))
print(len(crypted_pass))