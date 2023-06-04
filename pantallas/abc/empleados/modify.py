import customtkinter as tk

tk.set_appearance_mode('dark')
tk.set_default_color_theme('blue')

def open(row):
    screen = tk.CTkToplevel()
    screen.geometry('600x450')
    screen.title('Modificar usuario')

    def test():
        print('Hello')

    frame = tk.CTkFrame(master=screen)
    frame.pack(padx=120, pady=40, fill='both', expand=True)
    tk.CTkLabel(master=frame, text='Modificar usuario', font=('Roboto', 24)).pack(padx=10, pady=12)

    def create_elements():
        global entry_id
        global entry_nombre
        global entry_ap_p
        global entry_ap_m
        global entry_phone
        global entry_rol

        # Create elements
        entry_id = tk.CTkEntry(master=frame, placeholder_text='Número de empleado')
        entry_nombre = tk.CTkEntry(master=frame, placeholder_text='Nombre')
        entry_ap_p = tk.CTkEntry(master=frame, placeholder_text='Apellido paterno')
        entry_ap_m = tk.CTkEntry(master=frame, placeholder_text='Apellido materno')
        entry_phone = tk.CTkEntry(master=frame, placeholder_text='Número de teléfono')
        entry_rol = tk.CTkComboBox(master=frame)
        btn_accept = tk.CTkButton(master=frame, text='Confirmar')

        # Place elements
        entry_id.pack(padx=10, pady=5)
        entry_nombre.pack(padx=10, pady=5)
        entry_ap_p.pack(padx=10, pady=5)
        entry_ap_m.pack(padx=10, pady=5)
        entry_phone.pack(padx=10, pady=5)
        entry_rol.pack(padx=10, pady=5)
        btn_accept.pack(padx=10, pady=20)
    
    def setData():
        entries = [entry_id, entry_nombre, entry_ap_p, entry_ap_m, entry_phone]

        for x in range(len(entries)):
            entries[x].insert(0, str(row[x]))
    
    create_elements()
    setData()

    screen.grab_set()
    screen.mainloop()