#python week6_4



def menu():

    print("Choose option below:")
    print("1) Zero counter")
    print("2) Add count")
    print("3) Read count")
    print("0) Stop")
    option = int(input("Give your choice: "))
    return option
    
def addCount(count):
    print("Adding count.\n")
    count += 1
    return count

def zeroCount():
    print("Zeroing count.\n")
    count = 0
    return count

def readCount(count):
    print("Reading count.")
    print("Count is: "+str(count)+"\n") 
    return count

def main():
    print("This program acts like a typical counter.")

    choice = menu()
    count=0

    while(choice != 0):
        if(choice == 1):
            count=zeroCount()
            choice = menu()
            continue
        elif(choice == 2):
            count=addCount(count)
            choice = menu()
            continue
        elif(choice == 3 ):
            count=readCount(count)
            choice = menu()
            continue
        else:
            print("Unknown option, try again.\n")
            choice=menu()
            continue
            
    print("\nThank you for using the program.")
    
    return None


main()
            












