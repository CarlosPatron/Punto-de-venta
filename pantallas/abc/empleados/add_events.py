from werkzeug.security import generate_password_hash
from ..db_ev import database
from ..elements.elements import Empleado

def register_user(entries):
    db = database.Database()
    obj = Empleado()
    
    obj.nombre = entries[0].upper()
    obj.ap_p = entries[1].upper()
    obj.ap_m = entries[2].upper()
    obj.num_empleado = entries[3]
    obj.password = encrypt_password(entries[4])
    obj.phone = entries[5]
    obj.rol = entries[6]

    check = check_num_empleado(obj.num_empleado)

    if len(check)==0:
        db.addElement(obj, 'empleados', 'Empleado')
    else:
        return 1
    
    return 0

def check_num_empleado(num):
    db = database.Database()

    check =  db.getElementbyColumn('empleados', num, 'num_empleado')

    return check

def encrypt_password(password):
    crypted_pass = generate_password_hash(password)

    return crypted_pass