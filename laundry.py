from gpiozero import Button
from signal import pause

def detect():
    print("Hello!")

button = Button(18)
button.when_pressed = detect

pause()
