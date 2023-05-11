from ..db_ev import database

def get_all_table():
    db = database.Database()

    data_table = db.getTable('productos')

    return data_table