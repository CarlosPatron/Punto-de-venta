import customtkinter as tk
from tkinter import ttk
from .abc.productos import add, modify, add_inv, get_events

tk.set_appearance_mode('dark')
tk.set_default_color_theme('blue')

def open():
    screen = tk.CTkToplevel()
    screen.geometry('1280x720')
    screen.title('Inventario')

    def test():
        get_events.get_all_table()

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
        data = get_events.get_all_table()

        clear_treeview()
        
        for x in range(len(data)):
            tree.insert(parent='', index='end', iid=x, text='', values=(data[x][1], data[x][2], data[x][3], data[x][4], data[x][5], data[x][6]))
    
    def clear_treeview():
        for x in tree.get_children():
            tree.delete(x)
        screen.update()

    def press_add_button():
        add.open()
        fill_treeview()

        screen.grab_set()

    def bottom_menu():
        btn_add_inv = tk.CTkButton(master=frame, text='Agregar existencias', font=('Bold', 20), command=add_inv.open)
        btn_add = tk.CTkButton(master=frame, text='Registrar producto', font=('Bold', 20), command=press_add_button)
        btn_modify = tk.CTkButton(master=frame, text='Modificar producto', font=('Bold', 20), command=modify.open)
        btn_delete = tk.CTkButton(master=frame, text='Eliminar producto', font=('Bold', 20))
        btn_report = tk.CTkButton(master=frame, text='Generar reporte', font=('Bold', 20), command=test)

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