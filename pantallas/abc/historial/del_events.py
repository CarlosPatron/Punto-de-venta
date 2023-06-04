from ..db_ev import database, general_events

def delete_purchase(param):
    db = database.Database()

    id = general_events.get_element_id(param, table='ventas')
    db.deleteElement(table='ventas', id=id)