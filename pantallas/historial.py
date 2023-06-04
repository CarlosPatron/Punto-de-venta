import customtkinter as tk
from tkinter import ttk, messagebox
from .abc.historial import history_events as hiev
from .abc.historial import report_events, details, del_events

tk.set_appearance_mode('dark')
tk.set_default_color_theme('blue')

def open():
    screen = tk.CTkToplevel()
    screen.geometry('1280x720')
    screen.title('Historial de ventas')

    def test():
        print('Hello')

    frame = tk.CTkFrame(master=screen)
    frame.pack(padx=120, pady=40, fill='both', expand=True)
    tk.CTkLabel(master=frame, text='Ventas realizadas', font=('Roboto', 24)).pack(padx=10, pady=12)

    def create_treeview():
        global tree

        tree_columns = ('numero', 'importe', 'fecha', 'estado')
        tree = ttk.Treeview(master=frame, columns=tree_columns, show='headings')

        # Define headings
        tree.column('numero', anchor='center', stretch='no', width=200)
        tree.heading('numero', text='Número')

        tree.column('importe', anchor='center', stretch='no', width=200)
        tree.heading('importe', text='Importe')

        tree.column('fecha', anchor='center', stretch='no', width=200)
        tree.heading('fecha', text='Fecha')

        tree.column('estado', anchor='center', stretch='no', width=200)
        tree.heading('estado', text='Estado')

        # Place TreeView
        tree.pack(fill='both')

        # Other TreeView Configuration
        tree.config(height=25)
        style = ttk.Style()
        style.configure('Treeview.Heading', font=(None, 14))

    def fill_TreeView():
        clear_treeview()
        data = hiev.get_history()
        
        for x in range(len(data)):
            tree.insert(parent='', index='end', iid=x, text='', values=(data[x][0], data[x][3], data[x][5], data[x][6]))

    def clear_treeview():
        for x in tree.get_children():
            tree.delete(x)
        screen.update()

    def press_report():
        report_name = report_events.generate_report()
        messagebox.showinfo(title='Reporte generado', message=f'Reporte generado.\nNombre: {report_name}')

    def press_details():
        element = get_row()
        if len(element)==0:
            messagebox.showerror(title='Error', message='Se debe seleccionar una venta')
        else:
            id = element[0]
            details.open(id=id)

    def press_cancel():
        values = ['', 'id']
        try:
            values[0] = get_selected_item_column_value(0)

            if msgBox()=='yes':
                del_events.delete_purchase(values)
                fill_TreeView()
        except:
            messagebox.showerror(title='Error', message='Se debe seleccionar una venta')

    def msgBox():
        msg = messagebox.askquestion(title='Eliminar producto', message='¿Seguro que deseas eliminar el producto seleccionado?', icon='warning')
        
        return msg

    def get_selected_item_column_value(column):
        id_selected_item = tree.focus()
        value = tree.item(id_selected_item)['values'][column]

        return value

    def get_row():
        id_selected_item = tree.focus()
        value = tree.item(id_selected_item)['values']

        return value

    def create_bottom_menu():
        btn_detail = tk.CTkButton(master=frame, text='Ver detalles', font=('Bold', 20), command=press_details)
        btn_report = tk.CTkButton(master=frame, text='Generar reporte', font=('Bold', 20), command=press_report)
        btn_cancel = tk.CTkButton(master=frame, text='Cancelar venta', font=('Bold', 20), command=press_cancel)

        # Place buttons
        btn_detail.pack(padx=5, pady=5, side='left')
        btn_cancel.pack(padx=5, pady=5, side='left')
        btn_report.pack(padx=5, pady=5, side='left')

    create_treeview()
    create_bottom_menu()
    fill_TreeView()

    screen.grab_set()
    screen.mainloop()