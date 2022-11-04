#python week6_2
def outputInstructions():
    print("This program looks for the smaller input.")
    print("In the end, the program tells count of numbers inputted and the smallest number.")
    return 0

def askInteger():
    num = int(input("Give a new positive integer (0 stops): "))
    return num

def compareNumbers(num1,num2):
    if(num1>num2):
        smallest = num2
    else:
        smallest = num1
    return smallest

def outputResults():
    print("Thank you for using the program.")
    return None

def main():
    outputInstructions()
    Keeping = True
    integer = int(input("\nGive a positive integer: "))
    smallest = integer
    count=1

    while(Keeping):
        num2 = askInteger()
        if(num2 != 0):
            count +=1
            smallest = compareNumbers(smallest,num2)
        else:
            break

    if(count != 1):
         print("\nYou gave "+ str(count)+" numbers.")
         print("The smallest number was "+ str(smallest)+".")
    else:
         print("\nYou gave only one number, which was "+str(smallest)+".")
   

    outputResults()

    return None        


main()


