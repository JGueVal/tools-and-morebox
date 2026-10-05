# Auto-key press for the Pendemonium minigame in
#  the PSP game Work Time Fun (Beit Hell 2000).
# Keys are default controls for PPSSPP emulator.

# Install pynput with pip or package manager.
from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()

conta = 0
nootnootpingu = int(input("Repeat: "))

sleep(3)

# maybe lower times can be achieved. I haven't
#  tried with fastforward on.
while conta < nootnootpingu:
    print(conta,end="\r")
    sleep(0.26)
    keyboard.press('z')
    sleep(0.1)
    keyboard.release('z')
    sleep(0.01)
    keyboard.press('x')
    sleep(0.1)
    keyboard.release('x')
    conta += 1


# mppr. J.G.V.
