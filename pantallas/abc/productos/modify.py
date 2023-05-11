from tkinter import messagebox
import customtkinter as tk
from . import modify_events as moev

tk.set_appearance_mode('dark')
tk.set_default_color_theme('blue')

def open(element):
    screen = tk.CTkToplevel()
    screen.geometry('600x420')
    screen.title('Modificar producto')

    def pressAccept():
        new_entries = get_new_entries()
        code = moev.modify_product(element, new_entries)

        if code==0:
            pressCancel()
        else:
            messagebox.showerror(title='Producto ya registrado', message='El código pertenece a otro producto')

    def pressCancel():
        screen.quit()
        screen.destroy()
    
    def get_new_entries():
        new_entries = [entry_codigo.get(), entry_nombre.get(), entry_precio_compra.get(), entry_precio_venta.get(), entry_stock.get()]
        
        return new_entries

    def setData(element):
        entries = [entry_codigo, entry_nombre, entry_precio_compra, entry_precio_venta, entry_stock]

        for x in range(len(entries)):
            entries[x].insert(0, str(element[x]))

    frame = tk.CTkFrame(master=screen)
    frame.pack(padx=120, pady=40, fill='both', expand=True)
    tk.CTkLabel(master=frame, text='Modificar producto', font=('Roboto', 24)).pack(padx=10, pady=12)

    def create_elements():
        global entry_codigo
        global entry_nombre
        global entry_precio_compra
        global entry_precio_venta
        global entry_stock

        # Create elements
        entry_codigo = tk.CTkEntry(master=frame, placeholder_text='Código')
        entry_nombre = tk.CTkEntry(master=frame, placeholder_text='Nombre')
        entry_precio_compra = tk.CTkEntry(master=frame, placeholder_text='Precio de compra')
        entry_precio_venta = tk.CTkEntry(master=frame, placeholder_text='Precio de venta')
        entry_stock = tk.CTkEntry(master=frame, placeholder_text='Cantidad')
        btn_accept = tk.CTkButton(master=frame, text='Confirmar', command=pressAccept)
        btn_cancel = tk.CTkButton(master=frame, text='Cancelar', command=pressCancel)

        # Place elements
        entry_codigo.pack(padx=10, pady=5)
        entry_nombre.pack(padx=10, pady=5)
        entry_precio_compra.pack(padx=10, pady=5)
        entry_precio_venta.pack(padx=10, pady=5)
        entry_stock.pack(padx=10, pady=5)
        btn_accept.pack(padx=10, pady=20, side='left')
        btn_cancel.pack(padx=10, pady=20, side='right')
    
    create_elements()
    setData(element)

    screen.grab_set()
    screen.mainloop()