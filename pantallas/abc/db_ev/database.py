import mysql.connector

class Database:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = '123456'
        self.database = 'db_puntoventa'

    def connectDB(self):
        cnx = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database,
        )

        return cnx, cnx.cursor()
    
    def addElement(self, obj, table, opc):
        command = self.selectCmd(opc, table, obj, 'add')
        self.exeCmd(command, 'add')
    
    def getElementbyColumn(self, table, thing, column):
        command = f"SELECT * FROM {table} WHERE {column} = '{str(thing)}';"
        data = self.exeCmd(command, 'get')

        return data

    def getTable(self, table):
        command = f"SELECT * FROM {table} WHERE status = true;"
        data = self.exeCmd(command, 'get')

        return data

    def deleteElement(self, table, id):
        command = f"UPDATE {table} SET status = false WHERE id = {id};"
        self.exeCmd(command, 'delete')

    def updateElement(self, table, obj, opc):
        command = self.selectCmd(opc, table, obj, 'delete')
        self.exeCmd(command, 'update')

    def addStock(self, codigo, qty):
        command = f"UPDATE productos SET stock = {qty} WHERE codigo = '{codigo}'"
        self.exeCmd(command, type='update')

    def exeCmd(self, command, type):
        cnx, cursor = self.connectDB()

        cursor.execute(command)

        if type=='get':
            data = cursor.fetchall()
            return data
        else:
            cnx.commit()

        cnx.close()

    def selectCmd(self, opc, table, obj, action):
        if action=='add':
            if opc=='Producto':
                command = f"INSERT INTO {table} (codigo, nombre, precio_compra, precio_venta, stock, status) VALUES ('{obj.codigo}', '{obj.nombre}', {float(obj.precio_compra)}, {float(obj.precio_venta)}, {int(obj.stock)}, {obj.state});"
            elif opc=='Empleado':
                command = f"INSERT INTO {table} (nombre, ap_p, ap_m, phone, num_empleado, rol, status) VALUES ('{obj.nombre}', '{obj.ap_p}', '{obj.ap_m}', '{obj.phone}', {obj.num_empleado} '{obj.rol}', {obj.state});"
            elif opc=='Cliente':
                command = f"INSERT INTO {table} (nombre, ap_p, ap_m, phone, email, status) VALUES ('{obj.nombre}', '{obj.ap_p}', '{obj.ap_m}', '{obj.phone}', '{obj.email}', {obj.state});"
            elif opc=='Proveedor':
                command = f"INSERT INTO {table} (nombre, phone, email, status) VALUES ('{obj.nombre}', '{obj.phone}', '{obj.email}', {obj.state});"
            elif opc=='Sucursal':
                command = f"INSERT INTO {table} (nombre, direccion, phone, status) VALUES ('{obj.nombre}', '{obj.direccion}', '{obj.phone}, {obj.state}');"
        else:
            if opc=='Producto':
                command = f"UPDATE {table} SET codigo = '{obj.codigo}', nombre = '{obj.nombre}', precio_compra = {obj.precio_compra}, precio_venta = {obj.precio_venta}, stock = {obj.stock} WHERE id = {obj.id};"
            elif opc=='Empleado':
                command = f"UPDATE {table} SET nombre = '{obj.nombre}', ap_p = '{obj.ap_p}', ap_m = '{obj.ap_m}', phone = '{obj.phone}', num_empleado = '{obj.num_empleado}', rol = '{obj.rol}' WHERE id = {obj.id};"
            elif opc=='Cliente':
                command = f"UPDATE {table} SET nombre = '{obj.nombre}', ap_p = '{obj.ap_p}', ap_m = '{obj.ap_m}', phone = '{obj.phone}', email = '{obj.email}' WHERE id = {obj.id};"
            elif opc=='Proveedor':
                command = f"UPDATE {table} SET nombre = '{obj.nombre}', phone = '{obj.phone}', email = '{obj.email}' WHERE id = {obj.id};"
            elif opc=='Sucursal':
                command = f"UPDATE {table} SET nombre = '{obj.direccion}', phone = '{obj.phone}' WHERE id = {obj.id};"

        return command