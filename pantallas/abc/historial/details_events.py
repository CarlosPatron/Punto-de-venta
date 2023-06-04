from ..db_ev import database
from ..elements.elements import Venta, Producto
import ast

def get_data(id):
    db = database.Database()
    v = Venta()
    p = Producto()

    item = db.getElementbyId(table='ventas', id=id)
    products = []

    productsList = string_to_list(item[0][2])
    
    v.num = item[0][0]
    v.productos = productsList
    v.importe = item[0][3]
    v.descuento = item[0][4]
    v.fecha = item[0][5]
    v.state = item[0][6]

    for product in v.productos:
        p = get_products(item=product)
        products.append(p)

    return v, products

def get_products(item):
    db = database.Database()
    p = Producto()
    codigo = item[0]
    
    dbItem = db.getElementbyColumn(table='productos', thing=codigo, column='codigo')

    p.codigo = dbItem[0][1]
    p.nombre = dbItem[0][2]
    p.precio_venta = dbItem[0][4]
    p.stock = item[1]

    return p

def string_to_list(stringList):
    new_list =  ast.literal_eval(stringList)

    return new_list