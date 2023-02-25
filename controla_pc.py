from PIL import ImageGrab
import pyautogui
from flask import Flask, request
import requests
import time
import keyboard
from pynput import mouse

app = Flask(__name__) 

@app.route('/command', methods=['POST'])
def command():
    data = request.get_json()
    # process data and execute command
    x = data['x']
    y = data['y']
    command = data['command']

    time.sleep(2)
    pyautogui.moveTo(x, y)
    pyautogui.click(x, y)

    keyboard.write(command)
    pyautogui.press('enter')
    
    time.sleep(2)
    im = ImageGrab.grab()
    im.save("screenshot.png")
    
    send_screenshot()
    """
    updater.dispatcher.add_handler(CommandHandler('screenshot', send_screenshot))
    updater.start_polling()"""
    
    return 'Command executed'

def send_screenshot():
    requests.post('https://api.telegram.org/xxxxxxxxx:xxxxxxxxxx-xxxxxxxxxxxxxx/sendPhoto', # aqui ponemos la api de telegram
              files={
                'photo': ('E:\Python\Controlar_PC\screenshot.png', 
                open('E:\Python\Controlar_PC\screenshot.png', 'rb'))}, # Aqui agregan el path de donde guardaran la imagen
              data={'chat_id': 'xxxxxxxxx', 'caption': time.strftime("%c")}) # agregar su char ID 

def Press():
  count = 0
  OnClick()
  mouse.Listener(on_click=OnClick).start()

  while True:
      if(mouse_pressed[mouse.Button.left]):
        count+=1
        #print(str(count) + " boton izquierdo presionado")
        print(pyautogui.position())

mouse_pressed = dict.fromkeys((mouse.Button.left, mouse.Button.right, mouse.Button.unknown), False)
  
def OnClick(x, y, button, pressed):
    mouse_pressed[button]=pressed
    


if __name__ == '__main__':
    app.run(host='0.0.0.0')





















