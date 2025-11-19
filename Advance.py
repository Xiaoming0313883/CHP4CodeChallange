RED = '\033[31m'
RESET = '\033[0m'

def init():
    start = input("Enter a number to start counting: ")
    if not start.isdigit():
        print(f"{RED}Please enter a number{RESET}")
        init()
    else:
        countDown(int(start))

def countDown(number: int):
    while number >= 0:
        print(number)
        number -= 1
    print("Blast off!")

init()

