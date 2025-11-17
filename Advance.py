
import winsound

RED = '\033[31m'
RESET = '\033[0m'

def init():
    start = input("Enter a number to start counting: ")
    if not start.lstrip("-").isdigit(): #lstrip: remove leading characters from a string
        print(f"{RED}Please enter a number{RESET}")
        init()
    else:
        countDown(int(start.lstrip("-")),getSign(int(start)))

def countDown(number: int, sign: str):
    while number >= 0:
        print((sign if number != 0 else "") + str(number))
        number -= 1
    winsound.Beep(1000, 500)
    print("Blaze off!")

def getSign(number: int):
    if number < 0:
        return "-"
    return ""

init()


