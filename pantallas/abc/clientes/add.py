import customtkinter as tk
from tkinter import messagebox
from . import add_events as adev

tk.set_appearance_mode('dark')
tk.set_default_color_theme('blue')

def open():
    screen = tk.CTkToplevel()
    screen.geometry('600x450')
    screen.title('Agregar cliente')

    def on_press():
        entries = [entry_nombre.get(), entry_ap_p.get(), entry_ap_m.get(), entry_phone.get(), entry_email.get()]
        adev.add_client(entries=entries)

        messagebox.showinfo(title='Cliente rgistrado', message='Cliente registrado exitosamente')
        screen.quit()
        screen.destroy()

    frame = tk.CTkFrame(master=screen)
    frame.pack(padx=120, pady=40, fill='both', expand=True)
    tk.CTkLabel(master=frame, text='Agregar cliente', font=('Roboto', 24)).pack(padx=10, pady=12)

    def create_elements():
        # Globalize vars
        global entry_nombre
        global entry_ap_p
        global entry_ap_m
        global entry_phone
        global entry_email

        # Create elements
        entry_nombre = tk.CTkEntry(master=frame, placeholder_text='Nombre')
        entry_ap_p = tk.CTkEntry(master=frame, placeholder_text='Apellido paterno')
        entry_ap_m = tk.CTkEntry(master=frame, placeholder_text='Apellido materno')
        entry_phone = tk.CTkEntry(master=frame, placeholder_text='Número de teléfono')
        entry_email = tk.CTkEntry(master=frame, placeholder_text='Correo electrónico')
        btn_add = tk.CTkButton(master=frame, text='Agregar', command=on_press)

        # Place elements
        entry_nombre.pack(padx=10, pady=5)
        entry_ap_p.pack(padx=10, pady=5)
        entry_ap_m.pack(padx=10, pady=5)
        entry_phone.pack(padx=10, pady=5)
        entry_email.pack(padx=10, pady=5)
        btn_add.pack(padx=10, pady=20)
    
    create_elements()

    screen.grab_set()
    screen.mainloop()