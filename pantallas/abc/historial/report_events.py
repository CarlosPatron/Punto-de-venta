from ..db_ev import database, reports

def generate_report():
    data = [('Núm. Venta', 'Productos', 'Importe', 'Fecha', 'Estado')]

    db = database.Database()

    temp = db.getTable(table='ventas')

    for row in temp:
        data.append(row)

    name = reports.export_to_pdf(data=data, opt='Ventas')

    return name