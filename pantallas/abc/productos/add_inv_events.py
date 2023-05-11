from ..db_ev import database

def addStock(elements, new_qty):
    db = database.Database()

    codigo = elements[0]
    cantidad = int(elements[1]) + int(new_qty)

    db.addStock(codigo, cantidad)