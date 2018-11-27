from __future__ import print_function

import time
from termcolor import colored, cprint

def stdout(message, end="\n"):
    symbol = colored("resposta:", "yellow")
    currentime = colored("[{}]".format(time.strftime("%H:%M:%S")), "green")
    print("{} {} {}".format(symbol, currentime, message), end=end)

def showsign(message):    
    print(colored(message, "magenta"))




