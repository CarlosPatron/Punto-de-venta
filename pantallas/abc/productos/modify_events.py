from ..db_ev import database

def modify_product(obj, entrys):
    db = database.Database()
    db.updateElement('productos', obj, 'Producto')