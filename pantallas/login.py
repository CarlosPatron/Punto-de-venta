import customtkinter as tk

tk.set_appearance_mode('dark')
tk.set_default_color_theme('blue')

def open():
    screen = tk.CTkToplevel()
    screen.geometry('600x400')
    screen.title('Iniciar sesión')

    def test():
        print('Hello')

    frame = tk.CTkFrame(master=screen)
    frame.pack(padx=120, pady=40, fill='both', expand=True)
    tk.CTkLabel(master=frame, text='Iniciar sesión', font=('Roboto', 24)).pack(padx=10, pady=12)

    entry_user = tk.CTkEntry(master=frame, placeholder_text='Número de empleado')
    entry_password = tk.CTkEntry(master=frame, placeholder_text='Contraseña', show='•')
    btn_login = tk.CTkButton(master=frame, text='Iniciar sesión', command=test)

    # Place elements
    entry_user.pack(padx=10, pady=5)
    entry_password.pack(padx=10, pady=5)
    btn_login.pack(padx=10, pady=50, side='bottom')

    screen.grab_set()
    screen.mainloop()