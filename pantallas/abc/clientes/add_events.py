from ..db_ev import database
from ..elements.elements import Cliente

def add_client(entries):
    client = Cliente()
    db = database.Database()

    client.nombre = entries[0]
    client.ap_p = entries[1]
    client.ap_m = entries[2]
    client.phone = entries[3]
    client.email = entries[4]

    db.addElement(obj=client, table='clientes', opc='Cliente')