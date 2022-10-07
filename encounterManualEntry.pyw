import pyperclip
from win10toast import ToastNotifier
from pynput.keyboard import Key, Controller
import time
import d20
import csv

toaster = ToastNotifier()
keyboard = Controller()

#time.sleep(3)
#keyboard.type("test monster\t100\t10\t\t\t3\t")
#keyboard.type("lair\t10\t13\t\t\t1\t")

try:
    lines = pyperclip.paste().split('\n')
    reader = csv.reader(lines)
    for line in reader:
        if (len(line) < 2):
            raise Exception("fInvalid format. Use [qty],[name],<AC #>,<HP #>,<Init #>.  Use +/- prefix on initiative to roll.")


        qty = line[0]
        name = line[1]
        ac = ""
        hp = ""
        init = ""
        for item in line[2:5]:
            parts = item.strip().split(" ")
            match parts[0].strip().casefold():
                case "ac":
                    ac = parts[1]
                case "hp":
                    hp = parts[1]
                case "init":
                    init = parts[1]
        
        if init[0] == "-" or init[0] == "+":
            roll = d20.roll(f"1d20{init}")
            init = roll.total

        time.sleep(3)
        keyboard.type(f"{name}\t{hp}\t{ac}\t\t{init}\t{qty}\t")

except Exception as err:
    toaster.show_toast('Error', f'{err}', duration=10)
    exit()

