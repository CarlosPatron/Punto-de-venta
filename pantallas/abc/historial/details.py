import customtkinter as tk
from tkinter import ttk
from . import details_events

tk.set_appearance_mode('dark')
tk.set_default_color_theme('blue')

def open(id):
    screen = tk.CTkToplevel()
    screen.geometry('1280x720')
    screen.title('Vista detallada')

    def create_treeview():
        # TreeView
        global tree
        global lbl_precio
        tree_columns = ('codigo', 'cantidad', 'producto', 'precio_unitario', 'descuento', 'importe')
        treeFrame = tk.CTkFrame(master=screen)
        tree = ttk.Treeview(master=treeFrame, columns=tree_columns, show='headings')
        lbl_total = tk.CTkLabel(master=treeFrame, text='Total: $', font=('Roboto', 20))
        lbl_precio =  tk.CTkLabel(master=treeFrame, text='0', font=('Roboto', 20))

        # Define headings
        tree.column('codigo', anchor='center', stretch='no', width=200)
        tree.heading('codigo', text='Código')

        tree.column('cantidad', anchor='center', stretch='no', width=120)
        tree.heading('cantidad', text='Cantidad')

        tree.column('producto', anchor='center', width=500)
        tree.heading('producto', text='Producto')

        tree.column('precio_unitario', anchor='center', stretch='no', width=200)
        tree.heading('precio_unitario', text='Precio Unitario')

        tree.column('descuento', anchor='center', stretch='no', width=200)
        tree.heading('descuento', text='Descuento')

        tree.column('importe', anchor='center', stretch='no', width=300)
        tree.heading('importe', text='Importe')

        # Place TreeView
        treeFrame.pack(side='top', fill='both', padx=30, pady=20)
        tk.CTkLabel(master=treeFrame, text='Detalles de venta', font=('Roboto', 24)).pack(padx=10, pady=12)
        tree.pack(fill='both')
        lbl_precio.pack(padx=5, pady=5, side='right')
        lbl_total.pack(padx=5, pady=5, side='right')

        # Other TreeView Configuration
        tree.config(height=30)
        style = ttk.Style()
        style.configure('Treeview.Heading', font=(None, 14))

    def fill_TreeView():
        venta, productos = details_events.get_data(id)

        for x in range(len(productos)):
            product = productos[x]
            tree.insert(parent='', index='end', iid=x, text='', values=(product.codigo, product.stock, product.nombre, float(product.precio_venta), float(venta.descuento), float(product.stock)*float(product.precio_venta)))
        
        lbl_precio.configure(text=f'{venta.importe}')
    
    create_treeview()
    fill_TreeView()

    screen.grab_set()
    screen.mainloop()