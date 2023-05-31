import customtkinter as tk
from tkinter import messagebox
from . import code_events as coev

tk.set_appearance_mode('dark')
tk.set_default_color_theme('blue')

def open(tree):
    screen = tk.CTkToplevel()
    screen.geometry('450x300')
    screen.title('Código manual')
    screen.resizable(False, False)

    def on_press():
        last_iid = 0
        product = coev.search_product(entry_code.get())
        code, item = checkTreeView()

        if len(product)==0:
            messagebox.showerror(title='Error', message='Producto no encontrado')
        else:
            if len(tree.get_children())==0 or code=='':
                try:
                    last_iid = int(tree.get_children()[-1])
                except:
                    pass
                tree.insert(parent='', index='end', iid=last_iid+1, text='', values=(product[1], 1, product[2], float(product[4]), float(0), float(product[4])))
            else:
                qty = int(tree.set(item, 'cantidad'))
                tree.set(item, 'cantidad', qty+1)

            screen.quit()
            screen.destroy()
    
    def checkTreeView():
        code = ''
        given_code = entry_code.get()

        for item in tree.get_children():
            column_val =  tree.set(item, 'codigo')
            if given_code==column_val:
                code = given_code
                
                return code, item

        return code, ''

    frame = tk.CTkFrame(master=screen)
    frame.pack(padx=100, pady=40, fill='both', expand=True)
    tk.CTkLabel(master=frame, text='Escribir código', font=('Roboto', 24)).pack(padx=10, pady=12)

    entry_code = tk.CTkEntry(master=frame, placeholder_text='Código')
    btn_confirm = tk.CTkButton(master=frame, text='Aceptar', command=on_press)

    # Place elements
    entry_code.pack(padx=10, pady=5)
    btn_confirm.pack(padx=10, pady=50, side='bottom')

    screen.grab_set()
    screen.mainloop()