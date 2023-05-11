from ..db_ev import database
from ..elements.elements import Empleado

def register_user(entries):
    db = database.Database()
    obj = Empleado()
    
    obj.nombre = entries[0].upper()
    obj.ap_p = entries[1].upper()
    obj.ap_m = entries[2].upper()
    obj.num_empleado = entries[3]
    obj.phone = entries[4]
    obj.rol = entries[5]

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