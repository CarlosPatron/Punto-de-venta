import customtkinter as tk
from tkinter import ttk
from .abc.clientes import add, modify

tk.set_appearance_mode('dark')
tk.set_default_color_theme('blue')

def open():
    screen = tk.CTkToplevel()
    screen.geometry('1280x720')
    screen.title('Clientes')

    def test():
        print('Hello')

    frame = tk.CTkFrame(master=screen)
    frame.pack(padx=120, pady=40, fill='both', expand=True)
    tk.CTkLabel(master=frame, text='Clientes', font=('Roboto', 24)).pack(padx=10, pady=12)

    def create_treeview():
        global tree

        tree_columns = ('id', 'nombre', 'ap_p', 'ap_m', 'phone', 'email')
        tree = ttk.Treeview(master=frame, columns=tree_columns, show='headings')

        # Define headings
        tree.column('id', anchor='center', stretch='no', width=200)
        tree.heading('id', text='ID de empleado')

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
        btn_add = tk.CTkButton(master=frame, text='Agregar cliente', font=('Bold', 20), command=add.open)
        btn_modify = tk.CTkButton(master=frame, text='Modificar cliente', font=('Bold', 20), command=add.open)
        btn_delete = tk.CTkButton(master=frame, text='Eliminar cliente', font=('Bold', 20))
        btn_report = tk.CTkButton(master=frame, text='Generar reporte', font=('Bold', 20))

        btn_add.pack(padx=10, pady=5, side='left', anchor='sw')
        btn_modify.pack(padx=10, pady=5, side='left', anchor='sw')
        btn_delete.pack(padx=10, pady=5, side='left', anchor='sw')
        btn_report.pack(padx=10, pady=5, side='left', anchor='sw')
    
    create_treeview()
    bottom_menu()

    screen.grab_set()
    screen.mainloop()