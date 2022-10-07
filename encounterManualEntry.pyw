import pyperclip
from win10toast import ToastNotifier
from pynput.keyboard import Key, Controller
import time

toaster = ToastNotifier()
keyboard = Controller()

time.sleep(3)
keyboard.type("test monster\t100\t10\t\t\t3\t")
keyboard.type("lair\t10\t13\t\t\t1\t")

