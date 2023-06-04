from ..db_ev import database, reports

def generate_report():
    data = [('ID', 'Nombre', 'Ap. Paterno', 'Ap. Materno', 'Teléfono', 'Email', 'Estado')]

    db = database.Database()

    temp = db.getTable(table='clientes')

    for row in temp:
        data.append(row)

    #print(data)
    name = reports.export_to_pdf(data=data, opt='Clientes')

    return name