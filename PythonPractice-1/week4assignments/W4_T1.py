#python week4_1


print("Give two integers.")

firstnum= int(input("Give first number: "))
secondnum= int(input("Give second number: "))

print("Let's find out which number is greater.")

if(firstnum > secondnum):
    print("First number is greater.")
elif(firstnum<secondnum):
    print("Second number is greater.")
else:
    print("Numbers are the same.")

print("Let's find out if the numbers are even.")

if(firstnum%2==0):
    print("First number is even.")
else:
    print("First number is odd.")


if(secondnum%2==0):
    print("Second number is even.")
else:
    print("Second number is odd.")

print("Thank you for using the program.")
