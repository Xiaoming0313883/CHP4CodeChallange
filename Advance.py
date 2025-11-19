
def init():
    start = input("Enter a number to start counting: ")
    if not start.isdigit():
        print("Please enter a number")
        init()
    else:
        countDown(int(start))

def countDown(number: int):
    while number >= 0:
        print(number)
        number -= 1
    print("Blast off!")

init()

