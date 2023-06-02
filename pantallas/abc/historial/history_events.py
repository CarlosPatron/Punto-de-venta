from ..db_ev import database

def get_history():
    db = database.Database()

    db.connectDB()
    data = db.getTable(table='ventas')

    return data