import customtkinter as tk
from tkinter import ttk
from tkinter import messagebox
from .abc.productos import add, modify, add_inv, del_events, report_events
from .abc.db_ev import general_events as ge

tk.set_appearance_mode('dark')
tk.set_default_color_theme('blue')

def open():
    screen = tk.CTkToplevel()
    screen.geometry('1280x720')
    screen.title('Inventario')

    def test():
        ge.get_all_table('productos')

    frame = tk.CTkFrame(master=screen)
    frame.pack(padx=120, pady=40, fill='both', expand=True)
    tk.CTkLabel(master=frame, text='Inventario', font=('Roboto', 24)).pack(padx=10, pady=12)

    def create_treeview():
        global tree

        tree_columns = ('codigo', 'nombre', 'precio_compra', 'precio_venta', 'stock')
        tree = ttk.Treeview(master=frame, columns=tree_columns, show='headings')

        # Define headings
        tree.column('codigo', anchor='center', stretch='no', width=200)
        tree.heading('codigo', text='Código')

        tree.column('nombre', anchor='center', stretch='no', width=200)
        tree.heading('nombre', text='Nombre')

        tree.column('precio_compra', anchor='center', stretch='no', width=200)
        tree.heading('precio_compra', text='Precio de compra')

        tree.column('precio_venta', anchor='center', stretch='no', width=200)
        tree.heading('precio_venta', text='Precio de venta')

        tree.column('stock', anchor='center', stretch='no', width=200)
        tree.heading('stock', text='Cantidad disponible')

        # Place TreeView
        tree.pack(fill='both')

        # Other TreeView Configuration
        tree.config(height=25)
        style = ttk.Style()
        style.configure('Treeview.Heading', font=(None, 14))

    def fill_treeview():
        data = ge.get_all_table('productos')

        clear_treeview()
        
        for x in range(len(data)):
            tree.insert(parent='', index='end', iid=x, text='', values=(data[x][1], data[x][2], data[x][3], data[x][4], data[x][5], data[x][6]))
    
    def clear_treeview():
        for x in tree.get_children():
            tree.delete(x)
        screen.update()

    def press_add_inv_button():
        element = ['', 0]

        try:
            element[0] = get_selected_item_column_value(0)
            element[1] = get_selected_item_column_value(4)
            add_inv.open(element)
            fill_treeview()
        except:
            messagebox.showerror(title='Error', message='Se debe seleccionar un producto')

    def press_add_button():
        add.open()
        fill_treeview()

        screen.grab_set()

    def press_del_button():
        values = ['', 'codigo']
        try:
            values[0] = get_selected_item_column_value(0)

            if msgBox()=='yes':
                del_events.delete_product(values)
                fill_treeview()
        except:
            messagebox.showerror(title='Error', message='Se debe seleccionar un producto')
    
    def press_modify_button():
        element = get_row()
        if len(element)==0:
            messagebox.showerror(title='Error', message='Se debe seleccionar un producto')
        else:
            modify.open(element)
            fill_treeview()
            
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
    
    def report():
        report_name = report_events.generate_report()
        messagebox.showinfo(title='Reporte generado', message=f'Reporte guardado. Nombre: {report_name}')

    def bottom_menu():
        btn_add_inv = tk.CTkButton(master=frame, text='Agregar existencias', font=('Bold', 20), command=press_add_inv_button)
        btn_add = tk.CTkButton(master=frame, text='Registrar producto', font=('Bold', 20), command=press_add_button)
        btn_modify = tk.CTkButton(master=frame, text='Modificar producto', font=('Bold', 20), command=press_modify_button)
        btn_delete = tk.CTkButton(master=frame, text='Eliminar producto', font=('Bold', 20), command=press_del_button)
        btn_report = tk.CTkButton(master=frame, text='Generar reporte', font=('Bold', 20), command=report)

        btn_add_inv.pack(padx=10, pady=5, side='left', anchor='sw')
        btn_add.pack(padx=10, pady=5, side='left', anchor='sw')
        btn_modify.pack(padx=10, pady=5, side='left', anchor='sw')
        btn_delete.pack(padx=10, pady=5, side='left', anchor='sw')
        btn_report.pack(padx=10, pady=5, side='left', anchor='sw')
    
    create_treeview()
    bottom_menu()
    fill_treeview()

    screen.grab_set()
    screen.mainloop()