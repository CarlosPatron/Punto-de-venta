class Usuario:
    id = 0
    nombre = ''
    ap_p = ''
    ap_m = ''
    phone = ''
    state = 1

class Empleado(Usuario):
    num_empleado = ''
    password = ''
    rol = ''

class Cliente(Usuario):
    email = ''

class Proveedor:
    id = 0
    nombre = ''
    phone = ''
    email = ''
    state = 1

class Direccion:
    id = 0
    calle = ''
    calle1 = ''
    calle2 = ''
    zip_code = 0
    num_ext = 0
    num_int = 0

class Sucursal:
    id = 0
    nombre = ''
    direccion = Direccion
    phone = ''
    state = 1

class Producto:
    codigo = ''
    nombre = ''
    precio_compra = 0.0
    precio_venta = 0.0
    stock = 0
    state = 1

class Compra:
    id = 0
    productos = []
    importe = 0.0
    descuento = 0.0
    importe_iva = 0.0
    importe_total = 0.0
    state = 1


class Venta:
    id = 0
    productos = []
    importe = 0.0
    descuento = 0.0
    importe_iva = 0.0
    importe_total = 0.0
    pago_cliente = 0.0
    cambio = 0.0
    state = 1