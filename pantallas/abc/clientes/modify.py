import customtkinter as tk
from . import modify_events as moev

tk.set_appearance_mode('dark')
tk.set_default_color_theme('blue')

def open(element):
    screen = tk.CTkToplevel()
    screen.geometry('600x450')
    screen.title('Modificar cliente')

    frame = tk.CTkFrame(master=screen)
    frame.pack(padx=120, pady=40, fill='both', expand=True)
    tk.CTkLabel(master=frame, text='Modificar cliente', font=('Roboto', 24)).pack(padx=10, pady=12)

    def create_elements():
        # Globalize vars
        global entry_id
        global entry_nombre
        global entry_ap_p
        global entry_ap_m
        global entry_phone
        global entry_email

        # Create elements
        entry_id = tk.CTkEntry(master=frame, placeholder_text='ID de cliente')
        entry_nombre = tk.CTkEntry(master=frame, placeholder_text='Nombre')
        entry_ap_p = tk.CTkEntry(master=frame, placeholder_text='Apellido paterno')
        entry_ap_m = tk.CTkEntry(master=frame, placeholder_text='Apellido materno')
        entry_phone = tk.CTkEntry(master=frame, placeholder_text='Número de teléfono')
        entry_email = tk.CTkEntry(master=frame, placeholder_text='Correo electrónico')
        btn_accept = tk.CTkButton(master=frame, text='Confirmar', command=press_accept)

        # Place elements
        entry_id.pack(padx=10, pady=5)
        entry_nombre.pack(padx=10, pady=5)
        entry_ap_p.pack(padx=10, pady=5)
        entry_ap_m.pack(padx=10, pady=5)
        entry_phone.pack(padx=10, pady=5)
        entry_email.pack(padx=10, pady=5)
        btn_accept.pack(padx=10, pady=20)

    def press_accept():
        new_entries = get_new_entries()
        moev.modify_client(old_entries=element, new_entries=new_entries)
        screen.quit()
        screen.destroy()
    
    def set_data(element):
        entries = [entry_id, entry_nombre, entry_ap_p, entry_ap_m, entry_phone, entry_email]

        for x in range(len(entries)):
            entries[x].insert(0, str(element[x]))

    def get_new_entries():
        new_entries =  [entry_id.get(), entry_nombre.get(), entry_ap_p.get(), entry_ap_m.get(), entry_phone.get(), entry_email.get()]

        return new_entries
    
    create_elements()
    set_data(element=element)
    entry_id.configure(state="disabled")

    screen.grab_set()
    screen.mainloop()