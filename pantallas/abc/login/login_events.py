from werkzeug.security import check_password_hash # generate_password_hash
from ..db_ev import database

def check_login(num_empleado, password):
    db_pass = get_password(num_empleado)

    return check_password_hash(db_pass, password)

def get_password(num_empleado):
    db = database.Database()

    element = db.getElementbyColumn('empleados', num_empleado, 'num_empleado')
    password = element[0][2]

    return password