from werkzeug.security import generate_password_hash, check_password_hash

password = 'pass'
print('Password : ' + password)
hash_password = generate_password_hash(password)
print(hash_password)
print(check_password_hash(hash_password, 'wrong'))
print(
    len('pbkdf2:sha256:50000$Q26KbLEA$a403bfa53f6fbb1fc09fe5c2bd1a490e4c9614b748a2014d8c6a3f92210d9e45'
        ))
