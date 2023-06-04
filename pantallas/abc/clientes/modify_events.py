from ..db_ev import database, general_events
from ..elements.elements import Cliente

def modify_client(old_entries, new_entries):
    db = database.Database()
    client = Cliente()

    client.id = int(old_entries[0])
    client.nombre = str(new_entries[1])
    client.ap_p = str(new_entries[2])
    client.ap_m = str(new_entries[3])
    client.phone = str(new_entries[4])
    client.email = str(new_entries[5])

    db.updateElement(table='clientes', obj=client, opc='Cliente')