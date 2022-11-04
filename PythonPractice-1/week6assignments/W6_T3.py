#python week6_3



def menu():

    print("Choose option below:")
    print("1) Give a string")
    print("2) Give a hyphenate")
    print("3) Output results")
    print("0) Stop")
    option = int(input("Give your choice: "))
    return option
    
def askString():
    string = input("Give a string: \n")
    return string

def askHyphenate():
    hyphenate = input("Give a hyphenate: \n")
    return hyphenate

def outputResults(string,separator):
    lst = []
 
    for letter in string:
        lst.append(letter)

    for i in range(len(lst)-1):
        print(lst[i]+separator,end='')
        
    print(lst[i+1])

     
    return None

def main():
    print("This program can print strings with different hyphenates.")
    option = menu()
    
    while (option != 0):
            if(option == 1):
                string=askString()
                option = menu()
                continue
            elif(option == 2):
                separator = askHyphenate()
                option = menu()
                continue
            elif(option == 3):
                outputResults(string,separator)
                option = menu()
                continue
            elif(option == 0):
                break
            else:
                print("Unknown option, try again.\n")
                option = menu()
                continue

    print("\nThank you for using the program.")
    
    return None
    

main()
            












