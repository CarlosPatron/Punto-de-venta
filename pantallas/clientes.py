import customtkinter as tk
from tkinter import ttk, messagebox
from .abc.clientes import add, modify, del_events, report_events
from .abc.clientes.get_table import get_clients_data

tk.set_appearance_mode('dark')
tk.set_default_color_theme('blue')

def open():
    screen = tk.CTkToplevel()
    screen.geometry('1280x720')
    screen.title('Clientes')

    def press_add_button():
        add.open()
        fill_TreeView()

    def press_del_button():
        values = ['', 'id_cliente']
        try:
            values[0] = get_selected_item_column_value(0)

            if msgBox()=='yes':
                del_events.delete_product(values)
                fill_TreeView()
        except:
            messagebox.showerror(title='Error', message='Se debe seleccionar un cliente')

    def get_selected_item_column_value(column):
        id_selected_item = tree.focus()
        value = tree.item(id_selected_item)['values'][column]

        return value
    
    def report():
        report_events.generate_report()
    
    def msgBox():
        msg = messagebox.askquestion(title='Eliminar producto', message='¿Seguro que deseas eliminar el producto seleccionado?', icon='warning')
        
        return msg

    frame = tk.CTkFrame(master=screen)
    frame.pack(padx=120, pady=40, fill='both', expand=True)
    tk.CTkLabel(master=frame, text='Clientes', font=('Roboto', 24)).pack(padx=10, pady=12)

    def create_treeview():
        global tree

        tree_columns = ('id', 'nombre', 'ap_p', 'ap_m', 'phone', 'email')
        tree = ttk.Treeview(master=frame, columns=tree_columns, show='headings')

        # Define headings
        tree.column('id', anchor='center', stretch='no', width=200)
        tree.heading('id', text='ID de cliente')

        tree.column('nombre', anchor='center', stretch='no', width=200)
        tree.heading('nombre', text='Nombre')

        tree.column('ap_p', anchor='center', stretch='no', width=200)
        tree.heading('ap_p', text='Apellido paterno')

        tree.column('ap_m', anchor='center', stretch='no', width=200)
        tree.heading('ap_m', text='Apellido materno')

        tree.column('phone', anchor='center', stretch='no', width=200)
        tree.heading('phone', text='Número de teléfono')

        tree.column('email', anchor='center', stretch='no', width=200)
        tree.heading('email', text='Correo electrónico')

        # Place TreeView
        tree.pack(fill='both')

        # Other TreeView Configuration
        tree.config(height=25)
        style = ttk.Style()
        style.configure('Treeview.Heading', font=(None, 14))

    def bottom_menu():
        btn_add = tk.CTkButton(master=frame, text='Agregar cliente', font=('Bold', 20), command=press_add_button)
        btn_modify = tk.CTkButton(master=frame, text='Modificar cliente', font=('Bold', 20), command=add.open)
        btn_delete = tk.CTkButton(master=frame, text='Eliminar cliente', font=('Bold', 20), command=press_del_button)
        btn_report = tk.CTkButton(master=frame, text='Generar reporte', font=('Bold', 20), command=report)

        btn_add.pack(padx=10, pady=5, side='left', anchor='sw')
        btn_modify.pack(padx=10, pady=5, side='left', anchor='sw')
        btn_delete.pack(padx=10, pady=5, side='left', anchor='sw')
        btn_report.pack(padx=10, pady=5, side='left', anchor='sw')
    
    create_treeview()
    bottom_menu()

    def fill_TreeView():
        clear_treeview()
        data = get_clients_data()
        print(data)

        for x in range(len(data)):
            tree.insert(parent='', index='end', iid=x, text='', values=(data[x][0], data[x][1], data[x][2], data[x][3], data[x][4], data[x][5], data[x][6]))

    def clear_treeview():
        for x in tree.get_children():
            tree.delete(x)
        screen.update()

    fill_TreeView()

    screen.grab_set()
    screen.mainloop()