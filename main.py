from tkinter import ttk, messagebox
import threading
import keyboard
import customtkinter as tk
from pantallas import login, inventario, empleados, clientes
from pantallas.abc.codigo_manual import code

tk.set_appearance_mode('dark')
tk.set_default_color_theme('blue')

root = tk.CTk()
root.geometry('1280x720')
root.title('Punto de venta')
root.after(0, lambda:root.state('zoomed'))

t_add = threading.Thread(target=input_product_code)

#def input_product_code():
#    if keyboard.wait()
#        code = str(input())
#        print(code)

def press_user_button():
    login.open()

# ! Es sólo una simulación
def purchase():
    if len(tree.get_children())==0:
        messagebox.showerror(title='Error', message='Se debe agregar algún producto')
    else:
        messagebox.showinfo(title='Venta realizada', message='Venta realizada exitosamente')
        clear_treeView()

def press_code_button():
    code.open(tree)

def press_quit():
    selected = tree.focus()

    if len(selected)>0:
        tree.delete(selected)
    else:
        messagebox.showerror(title='Error', message='Se debe seleccionar un producto')

def cancel_sale():
    option = messagebox.askquestion(title='Cancelar venta', message='¿Estás seguro que deseas cancelar la venta?')
    
    if option=='yes':
        clear_treeView()

def clear_treeView():
    for x in tree.get_children():
        tree.delete(x)

def create_top_menu():
    global btn_user

    # Menu elements
    menu_items = ['btn_ventas','btn_inventario', 'btn_empleados', 'btn_clientes', 'btn_online']

    menuFrame = tk.CTkFrame(master=root)
    btn_ventas = tk.CTkButton(master=menuFrame, text='Historial de ventas', font=('Bold', 20))
    btn_inventario = tk.CTkButton(master=menuFrame, text='Inventario', font=('Bold', 20), command=inventario.open)
    btn_empleados = tk.CTkButton(master=menuFrame, text='Empleados', font=('Bold', 20), command=empleados.open)
    btn_clientes = tk.CTkButton(master=menuFrame, text='Clientes', font=('Bold', 20), command=clientes.open)
    btn_online = tk.CTkButton(master=menuFrame, text='Ventas en línea', font=('Bold', 20))

    #! empty_label = tk.CTkLabel(master=menuFrame, text="")
    btn_user = tk.CTkButton(master=menuFrame, text='Usuario', command=press_user_button)

    # Place menu items
    menuFrame.pack(side='top', fill='both', padx=30, pady=30)
    for x in range(len(menu_items)):
        exec(f"{menu_items[x]}.pack(side='left', padx=5, pady=5)")

    #! empty_label.grid(row=0, column=len(menu_items), sticky="ew")
    btn_user.pack(side='right', padx=5, pady=5)

def create_treeview():
    # TreeView
    global tree
    tree_columns = ('codigo', 'cantidad', 'producto', 'precio_unitario', 'descuento', 'importe')
    treeFrame = tk.CTkFrame(master=root)
    tree = ttk.Treeview(master=treeFrame, columns=tree_columns, show='headings')

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
    tree.pack(fill='both')

    # Other TreeView Configuration
    tree.config(height=30)
    style = ttk.Style()
    style.configure('Treeview.Heading', font=(None, 14))

def create_bottom_menu():
    # Globalize buttons
    global btn_cobrar
    global btn_cobrar_factura
    global btn_quitar_producto
    global btn_cancelar_venta
    global btn_introducir_codigo

    # Menu elements
    botMenuFrame = tk.CTkFrame(master=root)
    menu_items = ['btn_cobrar', 'btn_cobrar_factura', 'btn_quitar_producto', 'btn_cancelar_venta', 'btn_introducir_codigo']

    btn_cobrar = tk.CTkButton(master=botMenuFrame, text='✓ Cobrar', font=('Bold', 20), command=purchase)
    btn_cobrar_factura = tk.CTkButton(master=botMenuFrame, text='Cobrar con factura', font=('Bold', 20))
    btn_quitar_producto = tk.CTkButton(master=botMenuFrame, text='Quitar producto', font=('Bold', 20), command=press_quit)
    btn_cancelar_venta = tk.CTkButton(master=botMenuFrame, text='Cancelar venta', font=('Bold', 20), command=cancel_sale)
    btn_introducir_codigo = tk.CTkButton(master=botMenuFrame, text='Código manual', font=('Bold', 20), command=press_code_button)

    # Place items
    botMenuFrame.pack(side='bottom', fill='x', padx=30, pady=5)
    for x in range(len(menu_items)):
        exec(f"{menu_items[x]}.pack(side='left', padx=5, pady=5)")

create_top_menu()
create_treeview()
create_bottom_menu()
t_add.start()

root.mainloop()