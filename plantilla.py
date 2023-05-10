import customtkinter as tk

tk.set_appearance_mode('dark')
tk.set_default_color_theme('blue')

def open():
    screen = tk.CTkToplevel()
    screen.geometry('600x400')
    screen.title('Plantilla')

    def test():
        print('Hello')

    

    screen.mainloop()

open()