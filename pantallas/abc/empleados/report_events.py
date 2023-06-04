from ..db_ev import database, reports

def generate_report():
    data = [('Num. Empleado', 'Nombre', 'Ap. Paterno', 'Ap. Materno', 'Rol', 'Teléfono', 'Estado')]

    db = database.Database()

    temp = db.getTable(table='empleados')

    positions = [1, 3, 4, 5, 6, 7, 8]
    tempList = []
    elements = []

    for empleado in temp:
        for position in positions:
            tempList.append(empleado[position])
        elements.append(tempList)
        tempList = []

    for element in elements:
        data.append(element)

    name = reports.export_to_pdf(data=data, opt='Empleados')

    return name