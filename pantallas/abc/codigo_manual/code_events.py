from ..db_ev import database

def search_product(code):
    db = database.Database()

    data = db.getElementbyColumn('productos', code, 'codigo')

    if len(data)>0:
        product = data[0]
    else:
        return []

    return product
