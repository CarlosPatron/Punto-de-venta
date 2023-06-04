from ..db_ev import database, general_events

def delete_product(param):
    db = database.Database()

    id = general_events.get_element_id(param, table='clientes')
    db.deleteElement('clientes', id)