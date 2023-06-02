from tkinter import ttk, messagebox
import threading
import keyboard
import customtkinter as tk
from pantallas import login, inventario, empleados, clientes, historial
from pantallas.abc.codigo_manual import code
from pantallas.abc.codigo_manual import code_events as coev
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
        messagebox.showinfo(title='Venta realizada', message='Venta realizada exitosamente')
        clear_treeView()

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
    save_purchase(v)
    #print(f'Fecha: {v.fecha}\nProductos: {v.productos}\nImporte: {v.importe}\nDescuento: {v.descuento}\nCambio: {v.cambio}')

def save_purchase(obj):
    from pantallas.abc.db_ev import database

    db = database.Database()

    db.connectDB()
    sql = f"INSERT INTO ventas (num, productos, importe, descuento, fecha) VALUES ({int(obj.num)}, '{obj.productos}', {float(obj.importe)}, {float(obj.descuento)}, '{obj.fecha}');"
    db.exeCmd(command=sql, type='add')

def fill_purchase_object(obj, data):
    from datetime import datetime

    obj.importe = data[1]
    obj.descuento = data[0]
    obj.cambio = data[2]
    fecha = datetime.now()
    fechaFormato = fecha.strftime("%Y-%m-%d %H:%M:%S")
    obj.fecha = fechaFormato

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
        lbl_total.config(text='0')

def clear_treeView():
    for x in tree.get_children():
        tree.delete(x)

def press_historial():
    print()

def create_top_menu():
    global btn_user

    # Menu elements
    menu_items = ['btn_ventas','btn_inventario', 'btn_empleados', 'btn_clientes']

    menuFrame = tk.CTkFrame(master=root)
    btn_ventas = tk.CTkButton(master=menuFrame, text='Historial de ventas', font=('Bold', 20), command=historial.open)
    btn_inventario = tk.CTkButton(master=menuFrame, text='Inventario', font=('Bold', 20), command=inventario.open)
    btn_empleados = tk.CTkButton(master=menuFrame, text='Empleados', font=('Bold', 20), command=empleados.open)
    btn_clientes = tk.CTkButton(master=menuFrame, text='Clientes', font=('Bold', 20), command=clientes.open)
    #btn_online = tk.CTkButton(master=menuFrame, text='Ventas en línea', font=('Bold', 20))

    #! empty_label = tk.CTkLabel(master=menuFrame, text="")
    btn_user = tk.CTkButton(master=menuFrame, text='👤', font=('Roboto', 30), command=press_user_button)

    # Place menu items
    menuFrame.pack(side='top', fill='both', padx=30, pady=30)
    for x in range(len(menu_items)):
        exec(f"{menu_items[x]}.pack(side='left', padx=5, pady=5)")

    #! empty_label.grid(row=0, column=len(menu_items), sticky="ew")
    btn_user.pack(side='right', padx=5, pady=5)

def create_treeview():
    # TreeView
    global tree
    global lbl_total
    tree_columns = ('codigo', 'cantidad', 'producto', 'precio_unitario', 'descuento', 'importe')
    treeFrame = tk.CTkFrame(master=root)
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
    tree.pack(fill='both')
    lbl_precio.pack(padx=5, pady=5, side='right')
    lbl_total.pack(padx=5, pady=5, side='right')

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

def wait_string(e, array_code):
    if e.name=='enter':
        code = get_code(array_code)
        #print(f'Código: {code}')
        try:
            add_product(code=code, label=lbl_total)

        except:
            pass
        array_code.clear()
    else:
        if len(e.name)==1:
            array_code.append(e.name)

def get_code(array):
    code = ''.join(array)

    return code

stopThread = False

def threadFunction(array_code):
    global stopThread
    array_code = list(array_code)
    keyboard.on_press(lambda event: wait_string(event, array_code))
    while not stopThread:
        #if len(array_code)>0:
        #    code = ''.join(array_code)
        pass
        time.sleep(0.1)
    print('Hilo detenido')

def close_window():
    global stopThread

    stopThread = True
    thread.join()
    root.destroy()

root.protocol('WM_DELETE_WINDOW', close_window)

array_code = [""]
thread = threading.Thread(target=threadFunction, args=(array_code))
thread.start()

def stop_thread(arg):
    global stopThread
    global thread

    stopThread = True
    thread.join()
    print('Hilo detenido')

def start_thread(arg):
    global stopThread
    global thread

    stopThread = False
    thread.start()
    print('Hilo iniciado')

#root.bind('<FocusIn>', start_thread)
#root.bind('<FocusOut>', stop_thread)

def add_product(code, label):
    last_iid = 0
    product = coev.search_product(code)
    code, item = checkTreeView(code)

    if len(product)==0:
        messagebox.showerror(title='Error', message='Producto no encontrado')
    else:
        if len(tree.get_children())==0 or code=='':
            try:
                last_iid = int(tree.get_children()[-1])
            except:
                pass
            tree.insert(parent='', index='end', iid=last_iid+1, text='', values=(product[1], 1, product[2], float(product[4]), float(0), float(product[4])))
        else:
            qty = int(tree.set(item, 'cantidad'))
            tree.set(item, 'cantidad', qty+1)
            qty += 1
            print(qty)
            total = float(product[4])*qty
            print(total)
            tree.set(item, 'importe', float(product[4])*float(qty))
            text = tree.set(item, 'importe')
    
    #label.config(text=)

def checkTreeView(given_code):
        code = ''

        for item in tree.get_children():
            column_val =  tree.set(item, 'codigo')
            if given_code==column_val:
                code = given_code
                
                return code, item

        return code, ''

create_top_menu()
create_treeview()
create_bottom_menu()

root.mainloop()