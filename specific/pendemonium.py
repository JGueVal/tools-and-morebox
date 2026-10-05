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

# I tried with lower sleep times, but sometimes
#  it doesn't register putting the pen caps.
while conta < nootnootpingu:
    print(conta,end="\r")
    sleep(0.3)
    keyboard.press('z')
    sleep(0.1)
    keyboard.release('z')
    sleep(0.02)
    keyboard.press('x')
    sleep(0.1)
    keyboard.release('x')
    conta += 1


# mppr. J.G.V.
