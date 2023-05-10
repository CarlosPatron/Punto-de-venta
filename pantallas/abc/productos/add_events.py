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

    db.addElement(product, 'productos', 'Producto')