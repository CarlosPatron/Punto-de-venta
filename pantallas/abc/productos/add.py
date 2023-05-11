import customtkinter as tk
from . import add_events as ev
from tkinter import messagebox

tk.set_appearance_mode('dark')
tk.set_default_color_theme('blue')

def open():
    screen = tk.CTkToplevel()
    screen.geometry('600x420')
    screen.title('Registrar producto')

    def on_press():
        entrys = [entry_codigo.get(), entry_nombre.get(), entry_precio_compra.get(), entry_precio_venta.get(), entry_stock.get()]
        ev.add_product(entrys)
        messagebox.showinfo(message='Producto registrado exitosamente', title='Producto registrado')
        screen.quit()
        screen.destroy()

    frame = tk.CTkFrame(master=screen)
    frame.pack(padx=120, pady=40, fill='both', expand=True)
    tk.CTkLabel(master=frame, text='Registrar producto', font=('Roboto', 24)).pack(padx=10, pady=12)

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
        btn_add = tk.CTkButton(master=frame, text='Registrar', command=on_press)

        # Place elements
        entry_codigo.pack(padx=10, pady=5)
        entry_nombre.pack(padx=10, pady=5)
        entry_precio_compra.pack(padx=10, pady=5)
        entry_precio_venta.pack(padx=10, pady=5)
        entry_stock.pack(padx=10, pady=5)
        btn_add.pack(padx=10, pady=20)
    
    create_elements()

    screen.grab_set()
    screen.mainloop()