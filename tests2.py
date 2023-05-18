import keyboard

def wait_string(e):
    if e.name=='enter':
        print(code)
        code = ''
    else:
        if len(e.name)==1:
            code += str(e.name)

keyboard.on_press(wait_string)
while True:
    pass