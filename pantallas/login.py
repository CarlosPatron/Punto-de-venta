import customtkinter as tk
from tkinter import messagebox
from pantallas.abc.login import login_events as logev

tk.set_appearance_mode('dark')
tk.set_default_color_theme('blue')

def open():
    screen = tk.CTkToplevel()
    screen.geometry('600x400')
    screen.title('Iniciar sesión')
    screen.resizable(False, False)

    def on_press():
        num_empleado = entry_user.get()
        password = entry_password.get()

        if num_empleado=='' or password=='':
            messagebox.showerror(title='Datos incorrectos', message='Se deben llenar todos los campos')
        else:
            try:
                check = logev.check_login(num_empleado, password)
                if check==True:
                    messagebox.showinfo(title='Éxito', message='Se ha iniciado sesión exitosamente')
                    screen.quit()
                    screen.destroy()
                else:
                    messagebox.showerror(title='Datos incorrectos', message='Los datos de incio de sesión no coinciden')
            except:
                messagebox.showerror(title='Datos incorrectos', message='Los datos de incio de sesión no coinciden')
        

    def show_password():
        if show_pass.get()==1:
            entry_password.configure(show='')
        else:
            entry_password.configure(show='•')

    frame = tk.CTkFrame(master=screen)
    frame.pack(padx=120, pady=40, fill='both', expand=True)
    tk.CTkLabel(master=frame, text='Iniciar sesión', font=('Roboto', 24)).pack(padx=10, pady=12)

    entry_user = tk.CTkEntry(master=frame, placeholder_text='Número de empleado')
    entry_password = tk.CTkEntry(master=frame, placeholder_text='Contraseña', show='•')
    btn_login = tk.CTkButton(master=frame, text='Iniciar sesión', command=on_press)
    show_pass = tk.CTkCheckBox(master=frame, text='Mostrar contraseña', onvalue=1, offvalue=0, command=show_password)

    # Place elements
    entry_user.pack(padx=10, pady=5)
    entry_password.pack(padx=10, pady=5)
    show_pass.pack(padx=10, pady=5)
    btn_login.pack(padx=10, pady=50, side='bottom')

    screen.grab_set()
    screen.mainloop()