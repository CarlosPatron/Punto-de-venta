import itertools
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter

def grouper(iterable, n):
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args)

def export_to_pdf(data, opt):
    fecha = datetime.now()
    fechaFormato = fecha.strftime("%Y-%m-%d %H-%M-%S")
    name = f'Reporte{opt}-{fechaFormato}.pdf'
    c = canvas.Canvas(name, pagesize=A4)
    c.setTitle(name)
    w, h = A4
    max_rows_per_page = 45
    x_offset = 50
    y_offset = 50
    padding = 15

    xlist = [x + x_offset for x in [0, 30, 130, 260, 330, 400, 450, 500]]
    ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]

    for rows in grouper(data, max_rows_per_page):
        rows = tuple(filter(bool, rows))
        c.grid(xlist, ylist[:len(rows)+1])
        for y, row in zip(ylist[:-1], rows):
            for x, cell in zip(xlist, row):
                c.drawString(x, y-padding+3, str(cell))
        
        c.showPage()
    c.save()