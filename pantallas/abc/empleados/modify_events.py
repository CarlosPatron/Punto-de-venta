from ..db_ev import database
from ..elements.elements import Empleado

def modify_user(old_entries, new_entries):
    db = database.Database()
    user = Empleado()

    user.num_empleado = str(old_entries[0])
    user.nombre = str(new_entries[1])
    user.ap_p = str(new_entries[2])
    user.ap_m = str(new_entries[3])
    user.phone = str(new_entries[4])
    user.rol = str(new_entries[5])

    