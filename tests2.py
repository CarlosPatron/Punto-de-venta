import time
import keyboard

def wait_string(e):
    global array_code

    if e.name=='enter':
        code = get_code(array_code)
        print(f'Código: {code}')
        array_code = []
    else:
        if len(e.name)==1:
            array_code.append(e.name)

def get_code(array):
    code = ''.join(array)

    return code

keyboard.on_press(wait_string)
array_code = []

while True:
    #if len(array_code)>0:
    #    code = ''.join(array_code)
    pass
    time.sleep(0.1)