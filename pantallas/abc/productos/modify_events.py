from ..db_ev import database, general_events
from ..elements.elements import Producto

def modify_product(old_entries, new_entries):
    db = database.Database()
    product = Producto()

    product.codigo = str(old_entries[0])

    product.nombre = str(new_entries[1])
    product.precio_compra = float(new_entries[2])
    product.precio_venta = float(new_entries[3])
    product.stock = int(new_entries[4])

    values = [product.codigo, 'codigo']
    product.id = general_events.get_element_id(values)

    product.codigo = str(new_entries[0])
    db.updateElement('productos', product, 'Producto')