from tkinter import ttk, messagebox
import customtkinter as tk
from pantallas import login, inventario, empleados, clientes
from pantallas.abc.codigo_manual import code
from pantallas.abc.elements.elements import Venta
import time, keyboard, threading

tk.set_appearance_mode('dark')
tk.set_default_color_theme('blue')

root = tk.CTk()
root.geometry('1280x720')
root.title('Punto de venta')
root.after(0, lambda:root.state('zoomed'))

def press_user_button():
    login.open()

# ! Es sólo una simulación
def purchase():
    if len(tree.get_children())==0:
        messagebox.showerror(title='Error', message='Se debe agregar algún producto')
    else:
        register_purchase()
        #messagebox.showinfo(title='Venta realizada', message='Venta realizada exitosamente')
        #clear_treeView()

def register_purchase():
    tempList = []
    itemList = []
    data = [0.0, 0.0, 0.0]
    v = Venta()

    for item in tree.get_children():
        pList = tree.item(item)['values']
        tempList.append(pList[0])
        tempList.append(pList[1])

        itemList.append(tempList)
        data[0] += float(pList[4])
        data[1] += float(pList[5])
        data[2] += 0
        tempList = []

    fill_purchase_object(v, data)
    v.productos = itemList
    #print(f'Fecha: {v.fecha}\nProductos: {v.productos}\nImporte: {v.importe}\nDescuento: {v.descuento}\nCambio: {v.cambio}')

def fill_purchase_object(obj, data):
    from datetime import datetime

    obj.importe = data[1]
    obj.descuento = data[0]
    obj.cambio = data[2]
    obj.fecha = datetime.now()

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
    btn_user = tk.CTkButton(master=menuFrame, text='Usuario', border_width=0, command=press_user_button)

    # Place menu items
    menuFrame.pack(side='top', fill='both', padx=30, pady=30)
    for x in range(len(menu_items)):
        exec(f"{menu_items[x]}.pack(side='left', padx=5, pady=5)")

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

def wait_string(e, array_code):
    if e.name=='enter':
        code = get_code(array_code)
        print(f'Código: {code}')
        array_code.clear()
    else:
        if len(e.name)==1:
            array_code.append(e.name)

def get_code(array):
    code = ''.join(array)

    return code

def threadFunction(array_code):
    array_code = list(array_code)
    keyboard.on_press(lambda event: wait_string(event, array_code))
    while True:
        #if len(array_code)>0:
        #    code = ''.join(array_code)
        pass
        time.sleep(0.1)

array_code = [""]
thread = threading.Thread(target=threadFunction, args=(array_code))
thread.start()

# Other config
root.grid_columnconfigure(0, weight=1)

root.mainloop()