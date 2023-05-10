import customtkinter as tk
from tkinter import ttk
from .abc.productos import add, modify

tk.set_appearance_mode('dark')
tk.set_default_color_theme('blue')

def open():
    screen = tk.CTkToplevel()
    screen.geometry('1280x720')
    screen.title('Inventario')

    def test():
        print('Hello')

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

    def bottom_menu():
        btn_add = tk.CTkButton(master=frame, text='Agregar producto', font=('Bold', 20), command=add.open)
        btn_modify = tk.CTkButton(master=frame, text='Modificar producto', font=('Bold', 20), command=modify.open)
        btn_delete = tk.CTkButton(master=frame, text='Eliminar producto', font=('Bold', 20))
        btn_report = tk.CTkButton(master=frame, text='Generar reporte', font=('Bold', 20))

        btn_add.pack(padx=10, pady=5, side='left', anchor='sw')
        btn_modify.pack(padx=10, pady=5, side='left', anchor='sw')
        btn_delete.pack(padx=10, pady=5, side='left', anchor='sw')
        btn_report.pack(padx=10, pady=5, side='left', anchor='sw')
    
    create_treeview()
    bottom_menu()

    screen.grab_set()
    screen.mainloop()