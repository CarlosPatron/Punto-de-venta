import customtkinter as tk
from tkinter import ttk
from .abc.historial import history_events as hiev

tk.set_appearance_mode('dark')
tk.set_default_color_theme('blue')

def open():
    screen = tk.CTkToplevel()
    screen.geometry('1280x720')
    screen.title('Historial de ventas')

    def test():
        print('Hello')

    frame = tk.CTkFrame(master=screen)
    frame.pack(padx=120, pady=40, fill='both', expand=True)
    tk.CTkLabel(master=frame, text='Ventas realizadas', font=('Roboto', 24)).pack(padx=10, pady=12)

    def create_treeview():
        global tree

        tree_columns = ('numero', 'importe', 'fecha', 'estado')
        tree = ttk.Treeview(master=frame, columns=tree_columns, show='headings')

        # Define headings
        tree.column('numero', anchor='center', stretch='no', width=200)
        tree.heading('numero', text='Número')

        tree.column('importe', anchor='center', stretch='no', width=200)
        tree.heading('importe', text='Importe')

        tree.column('fecha', anchor='center', stretch='no', width=200)
        tree.heading('fecha', text='Fecha')

        tree.column('estado', anchor='center', stretch='no', width=200)
        tree.heading('estado', text='Estado')

        # Place TreeView
        tree.pack(fill='both')

        # Other TreeView Configuration
        tree.config(height=25)
        style = ttk.Style()
        style.configure('Treeview.Heading', font=(None, 14))

    def fill_TreeView():
        clear_treeview()
        data = hiev.get_history()
        
        for x in range(len(data)):
            tree.insert(parent='', index='end', iid=x, text='', values=(data[x][0], data[x][3], data[x][5], data[x][6]))

    def clear_treeview():
        for x in tree.get_children():
            tree.delete(x)
        screen.update()

    create_treeview()
    fill_TreeView()

    screen.mainloop()