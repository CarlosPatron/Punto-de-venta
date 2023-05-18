import keyboard
import threading

codes = []

def wait_string():
    while True:
        codes.append(keyboard.read_key())
        
        print(codes)

t1 = threading.Thread(target=wait_string)
t1.start()