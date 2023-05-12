import customtkinter as tk
from tkinter import messagebox
from . import add_events as addev

tk.set_appearance_mode('dark')
tk.set_default_color_theme('blue')

def open():
    screen = tk.CTkToplevel()
    screen.geometry('600x470')
    screen.title('Registrar usuario')
    screen.resizable(False, False)

    def on_press():
        entries_data = [entry_nombre.get(), entry_ap_p.get(), entry_ap_m.get(), entry_num_emp.get(), entry_password.get(), entry_phone.get(), entry_rol.get()]
        check = check_empty_entries(entries_data)

        if check==0:
            code = addev.register_user(entries_data)

            if code==0:
                messagebox.showinfo(message='Empleado registrado exitosamente', title='Empleado registrado')
                screen.quit()
                screen.destroy()
            else:
                messagebox.showerror(title='Número ocupado', message='El número de empleado ya se encuentra registrado')
        else:
            messagebox.showerror(title='Error', message='Se deben llenar todos los campos')

    def check_empty_entries(entries):
        for x in entries:
            if len(x)==0:
                return 1
        
        return 0

    frame = tk.CTkFrame(master=screen)
    frame.pack(padx=120, pady=40, fill='both', expand=True)
    tk.CTkLabel(master=frame, text='Agregar usuario', font=('Roboto', 24)).pack(padx=10, pady=12)

    def create_elements():
        global entry_nombre
        global entry_ap_p
        global entry_ap_m
        global entry_num_emp
        global entry_password
        global entry_phone
        global entry_rol

        # Create elements
        entry_nombre = tk.CTkEntry(master=frame, placeholder_text='Nombre')
        entry_ap_p = tk.CTkEntry(master=frame, placeholder_text='Apellido paterno')
        entry_ap_m = tk.CTkEntry(master=frame, placeholder_text='Apellido materno')
        entry_num_emp = tk.CTkEntry(master=frame, placeholder_text='Número de empleado')
        entry_password = tk.CTkEntry(master=frame, show='•', placeholder_text='Contraseña')
        entry_phone = tk.CTkEntry(master=frame, placeholder_text='Número de teléfono')
        entry_rol = tk.CTkComboBox(master=frame, values=['USUARIO', 'ADMIN'])
        btn_add = tk.CTkButton(master=frame, text='Registrar', command=on_press)

        # Place elements
        entry_nombre.pack(padx=10, pady=5)
        entry_ap_p.pack(padx=10, pady=5)
        entry_ap_m.pack(padx=10, pady=5)
        entry_num_emp.pack(padx=10, pady=5)
        entry_password.pack(padx=10, pady=5)
        entry_phone.pack(padx=10, pady=5)
        entry_rol.pack(padx=10, pady=5)
        btn_add.pack(padx=10, pady=20)
    
    create_elements()

    screen.grab_set()
    screen.mainloop()