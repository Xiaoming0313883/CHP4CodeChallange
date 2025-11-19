import time

from tqdm import tqdm #pip install tqdm
import winsound

RED = '\033[31m'
RESET = '\033[0m'

def init():
    start = input("Enter a number to start counting: ")
    if not start.lstrip("-").isdigit(): #lstrip: remove leading characters from a string
        print(f"{RED}Please enter a number{RESET}")
        init()
    else:
        countDown(int(start.lstrip("-")))

def countDown(number: int):
    pbar = tqdm(range(number)) #declare progress bar
    pbar.update(number) #update progress bar max value to number
    pbar.refresh() #refresh progress bar
    while number >= 0:
        pbar.n = number #set current progress bar value as number
        pbar.refresh() #refresh progress bar
        time.sleep(1) #sleep 1 second
        number -= 1
    winsound.Beep(1000, 500)
    print("Blast off!")

init()


