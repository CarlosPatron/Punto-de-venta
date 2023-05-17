from .database import Database

def get_element_id(values, table):
    thing = str(values[0])
    column = values[1]

    db = Database()

    data = db.getElementbyColumn(table, thing, column)
    id = data[0][0]

    return id

def get_all_table(table):
    db = Database()

    data_table = db.getTable(table)

    return data_table