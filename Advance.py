
def init():
    start = input("Enter a number to start counting: ")
    countDown(int(start))

def countDown(number: int):
    while number >= 0:
        print(number)
        number -= 1
    print("Blaze off!")

init()

