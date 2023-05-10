import customtkinter as tk

tk.set_appearance_mode('dark')
tk.set_default_color_theme('blue')

def open():
    screen = tk.CTkToplevel()
    screen.geometry('600x420')
    screen.title('Modificar producto')

    def test():
        print('Hello')

    frame = tk.CTkFrame(master=screen)
    frame.pack(padx=120, pady=40, fill='both', expand=True)
    tk.CTkLabel(master=frame, text='Modificar producto', font=('Roboto', 24)).pack(padx=10, pady=12)

    def create_elements():
        # Create elements
        entry_codigo = tk.CTkEntry(master=frame, placeholder_text='Código')
        entry_nombre = tk.CTkEntry(master=frame, placeholder_text='Nombre')
        entry_precio_compra = tk.CTkEntry(master=frame, placeholder_text='Precio de compra')
        entry_precio_venta = tk.CTkEntry(master=frame, placeholder_text='Precio de venta')
        entry_stock = tk.CTkEntry(master=frame, placeholder_text='Cantidad')
        btn_accept = tk.CTkButton(master=frame, text='Confirmar')

        # Place elements
        entry_codigo.pack(padx=10, pady=5)
        entry_nombre.pack(padx=10, pady=5)
        entry_precio_compra.pack(padx=10, pady=5)
        entry_precio_venta.pack(padx=10, pady=5)
        entry_stock.pack(padx=10, pady=5)
        btn_accept.pack(padx=10, pady=20)
    
    create_elements()

    screen.grab_set()
    screen.mainloop()