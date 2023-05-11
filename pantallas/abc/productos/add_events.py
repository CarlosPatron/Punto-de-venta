from ..db_ev import database
from ..elements.elements import Producto

def add_product(entrys):
    product = Producto()
    db = database.Database()

    product.codigo = entrys[0]
    product.nombre = entrys[1]
    product.precio_compra = entrys[2]
    product.precio_venta = entrys[3]
    product.stock = entrys[4]

    check = check_not_registered(product.codigo)
    
    if len(check)==0:
        db.addElement(product, 'productos', 'Producto')
    else:
        return 1
    
    return 0

def check_not_registered(codigo):
    db = database.Database()

    check = db.getElementbyColumn('productos', codigo, 'codigo')

    return check