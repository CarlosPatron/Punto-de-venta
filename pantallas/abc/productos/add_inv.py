import customtkinter as tk

tk.set_appearance_mode('dark')
tk.set_default_color_theme('blue')

def open():
    screen = tk.CTkToplevel()
    screen.geometry('450x300')
    screen.title('Añadir stock')

    def test():
        print('Hello')

    frame = tk.CTkFrame(master=screen)
    frame.pack(padx=100, pady=40, fill='both', expand=True)
    tk.CTkLabel(master=frame, text='Agregar existencias', font=('Roboto', 24)).pack(padx=10, pady=12)

    entry_qty = tk.CTkEntry(master=frame, placeholder_text='Cantidad')
    btn_confirm = tk.CTkButton(master=frame, text='Confirmar', command=test)

    # Place elements
    entry_qty.pack(padx=10, pady=5)
    btn_confirm.pack(padx=10, pady=50, side='bottom')

    screen.grab_set()
    screen.mainloop()