from .database import Database

def get_element_id(values):
    thing = str(values[0])
    column = values[1]

    db = Database()

    data = db.getElementbyColumn('productos', thing, column)
    id = data[0][0]

    return id