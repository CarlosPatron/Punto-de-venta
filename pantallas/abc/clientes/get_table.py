from ..db_ev import database

def get_clients_data():
    db = database.Database()

    data = db.getTable(table='clientes')

    return data