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
        command = self.selectCmd(opc, table, obj)
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

    # Falta terminar la sentencia
    def updateElement(self, table, obj):
        command = f"UPDATE {table} "
        self.exeCmd(command, 'update')

    def exeCmd(self, command, type):
        cnx, cursor = self.connectDB()

        cursor.execute(command)

        if type=='get':
            data = cursor.fetchall()
            return data
        else:
            cnx.commit()

        cnx.close()

    def selectCmd(self, opc, table, obj):
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

        return command