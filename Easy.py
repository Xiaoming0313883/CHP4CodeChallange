#request user input the initial number to count
start = int(input("Enter a number to start counting: "))

#loop start with the number that user input
#loop until the counter become zero
while start >= 0:
    print(start) #print the counting number
    start-=1 #minus 1 after counted
print("Blast off!") #when the loop is end,
                    #mean that counted until
                    #zero