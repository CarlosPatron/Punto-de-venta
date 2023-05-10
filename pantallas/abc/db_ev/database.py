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
        self.exeCmd(command)
    
    def getElementbyId(self, table, id, column):
        command = f"SELECT * FROM {table} WHERE {column} = {str(id)};"
        self.exeCmd(command)

    def getTable(self, table):
        command = f"SELECT * FROM {table};"
        self.exeCmd(command)

    def deleteElement(self, table, id, column):
        command = f"DELETE FROM {table} WHERE {column} = {str(id)};"
        self.exeCmd(command)

    def exeCmd(self, command):
        cnx, cursor = self.connectDB()

        cursor.execute(command)
        cnx.commit()
        cnx.close()

    def selectCmd(self, opc, table, obj):
        if opc=='Producto':
            command = f"INSERT INTO {table} (codigo, nombre, precio_compra, precio_venta, stock) VALUES ('{obj.codigo}', '{obj.nombre}', {float(obj.precio_compra)}, {float(obj.precio_venta)}, {int(obj.stock)});"
        elif opc=='Empleado':
            command = f"INSERT INTO {table} (nombre, ap_p, ap_m, phone, rol) VALUES ('{obj.nombre}', '{obj.ap_p}', '{obj.ap_m}', '{obj.phone}', '{obj.rol}');"
        elif opc=='Cliente':
            command = f"INSERT INTO {table} (nombre, ap_p, ap_m, phone, email) VALUES ('{obj.nombre}', '{obj.ap_p}', '{obj.ap_m}', '{obj.phone}', '{obj.email}');"
        elif opc=='Proveedor':
            command = f"INSERT INTO {table} (nombre, phone, email) VALUES ('{obj.nombre}', '{obj.phone}', '{obj.email}');"
        elif opc=='Sucursal':
            command = f"INSERT INTO {table} (nombre, direccion, phone) VALUES ('{obj.nombre}', '{obj.direccion}', '{obj.phone}');"

        return command