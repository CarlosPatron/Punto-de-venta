from ..db_ev import database, general_events

def delete_user(param):
    db = database.Database()

    id = general_events.get_element_id(param)
    db.deleteElement('empleados', id)