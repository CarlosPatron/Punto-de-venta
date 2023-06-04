from ..db_ev import database, reports
from ..elements.elements import Venta

def generate_report():
    data = [('Núm. Venta', 'Importe', 'Fecha', 'Estado')]

    db = database.Database()

    temp = db.getTable(table='ventas')

    positions = [0, 3, 5, 6]
    tempList = []
    elements = []

    for venta in temp:
        for position in positions:
            tempList.append(venta[position])
        elements.append(tempList)
        tempList = []

    for element in elements:
        data.append(element)

    name = reports.export_to_pdf(data=data, opt='Ventas')

    return name