#python week4_4


print("This is a menu driven program, where you can choose which operation the program performs.")
print("Choose the operation below:")

print("1) Print welcome message")
print("2) Print a string")
print("3) Print a string backwards")
print("4) Print string length")
print("0) Exit")

option1= input("Give option: ")

if(option1.isdigit()):
    option=int(option1)
    if(option==1):
        print("Welcome user!")
    elif(option==2):
        str1=input("Give string: ")
        print("String you gave "+"\'"+str1+"\'.")
    elif(option==3):
        str1=input("Give string: ")
        print("String you gave backwards "+"\'"+str1[::-1]+"\'.")
    elif(option==4):
        str1=input("Give string: ")
        print("String length is",str(len(str1)),"characters.")
    elif(option==0):
        print("Exiting!")
    else:
        print("Unknown option.")
else:
    nothing=0


print("Thank you for using the program.")
