import time
import winsound

RED = '\033[31m'
RESET = '\033[0m'

def init():
    start = input("Enter a number to start counting: ")
    if not start.lstrip("-").isdigit():
        print(f"{RED}Please enter a number{RESET}")
        init()
    else:
        countDown(int(start.lstrip("-")))

def countDown(number: int):
    while number >= 0:
        mins = number // 60
        secs = number % 60
        print(f"{mins:02}:{secs:02}")
        time.sleep(1)
        number -= 1
    winsound.Beep(1000, 500)
    print("Blaze off!")

def getSign(number: int):
    if number < 0:
        return "-"
    return ""

init()