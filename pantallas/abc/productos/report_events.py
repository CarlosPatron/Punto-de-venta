from ..db_ev import database
from ..db_ev import reports

def generate_report():
    data = [('ID', 'Código', 'Nombre', 'P. Compra', 'P. Venta', 'Stock', 'Estado')]

    db = database.Database()

    temp = db.getTable(table='productos')

    for row in temp:
        data.append(row)

    #print(data)
    reports.export_to_pdf(data=data, opt='Productos')