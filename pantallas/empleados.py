import customtkinter as tk
from tkinter import ttk, messagebox
from .abc.empleados import add, modify, del_events, report_events
from .abc.db_ev import general_events as ge

tk.set_appearance_mode('dark')
tk.set_default_color_theme('blue')

def open():
    screen = tk.CTkToplevel()
    screen.geometry('1280x720')
    screen.title('Empleados')

    def fill_treeView():
        data = ge.get_all_table('empleados')

        clear_treeView()

        for x in range(len(data)):
            tree.insert(parent='', index='end', iid=x, text='', values=(data[x][1], data[x][3], data[x][4], data[x][5], data[x][6], data[x][8]))
    
    def clear_treeView():
        for x in tree.get_children():
            tree.delete(x)

    def press_add_button():
        add.open()
        fill_treeView()

    def press_modify_button():
        element = get_row()

        if len(element)==0:
            messagebox.showerror(title='Error', message='Se debe seleccionar un empleado')
        else:
            modify.open(row=element)
            fill_treeView()

    def press_del_button():
        values = ['', 'num_empleado']

        try:
            values[0] = get_selected_item_column_value(0)

            if msgBox()=='yes':
                del_events.delete_user(values)
                fill_treeView()
        except:
            messagebox.showerror(title='Error', message='Se debe seleccionar un empleado')

    def press_report():
        report_name = report_events.generate_report()
        messagebox.showinfo(title='Reporte generado', message=f'Nombre: {report_name}')

    def msgBox():
        msg = messagebox.askquestion(title='Eliminar empleado', message='¿Seguro que deseas eliminar a este empleado?', icon='warning')

        return msg

    def get_selected_item_column_value(column):
        id_selected_item = tree.focus()
        value = tree.item(id_selected_item)['values'][column]

        return value

    def get_row():
        focus = tree.focus()
        item = tree.item(focus)['values']

        return item

    frame = tk.CTkFrame(master=screen)
    frame.pack(padx=120, pady=40, fill='both', expand=True)
    tk.CTkLabel(master=frame, text='Usuarios', font=('Roboto', 24)).pack(padx=10, pady=12)

    def create_treeview():
        global tree

        tree_columns = ('num_empleado', 'nombre', 'ap_p', 'ap_m', 'rol', 'phone')
        tree = ttk.Treeview(master=frame, columns=tree_columns, show='headings')

        # Define headings
        tree.column('num_empleado', anchor='center', stretch='no', width=200)
        tree.heading('num_empleado', text='ID de empleado')

        tree.column('nombre', anchor='center', stretch='no', width=200)
        tree.heading('nombre', text='Nombre')

        tree.column('ap_p', anchor='center', stretch='no', width=200)
        tree.heading('ap_p', text='Apellido paterno')

        tree.column('ap_m', anchor='center', stretch='no', width=200)
        tree.heading('ap_m', text='Apellido materno')

        tree.column('rol', anchor='center', stretch='no', width=200)
        tree.heading('rol', text='Rol')

        tree.column('phone', anchor='center', stretch='no', width=200)
        tree.heading('phone', text='Número de teléfono')

        # Place TreeView
        tree.pack(fill='both')

        # Other TreeView Configuration
        tree.config(height=25)
        style = ttk.Style()
        style.configure('Treeview.Heading', font=(None, 14))

    def bottom_menu():
        btn_add = tk.CTkButton(master=frame, text='Agregar usuario', font=('Bold', 20), command=press_add_button)
        btn_modify = tk.CTkButton(master=frame, text='Modificar usuario', font=('Bold', 20), command=press_modify_button)
        btn_delete = tk.CTkButton(master=frame, text='Eliminar usuario', font=('Bold', 20), command=press_del_button)
        btn_report = tk.CTkButton(master=frame, text='Generar reporte', font=('Bold', 20), command=press_report)

        btn_add.pack(padx=10, pady=5, side='left', anchor='sw')
        btn_modify.pack(padx=10, pady=5, side='left', anchor='sw')
        btn_delete.pack(padx=10, pady=5, side='left', anchor='sw')
        btn_report.pack(padx=10, pady=5, side='left', anchor='sw')
    
    create_treeview()
    bottom_menu()
    fill_treeView()

    screen.grab_set()
    screen.mainloop()