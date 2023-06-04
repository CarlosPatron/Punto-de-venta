import keyboard, threading, time

def wait_string(e, array_code):
    if e.name=='enter':
        code = get_code(array_code)
        print(f'Código: {code}')
        array_code.clear()
    else:
        if len(e.name)==1:
            array_code.append(e.nam.e)

def get_code(array):
    code = ''.join(array)

    return code

stopThread = False

def threadFunction(array_code):
    global stopThread
    array_code = list(array_code)
    keyboard.on_press(lambda event: wait_string(event, array_code))
    while stopThread==False:
        #if len(array_code)>0:
        #    code = ''.join(array_code)
        pass
        time.sleep(0.1)

array_code = [""]
thread = threading.Thread(target=threadFunction, args=(array_code))
thread.start()