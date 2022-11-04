#python week5_3 


exitCode=0
totalCoin=0

while (exitCode >=0):
    exitCode = int(input("Insert 3 - 7 coins (0 stops): "))
    if (exitCode == 0):
        print("Amount of coins inserted:",str(totalCoin)+".")
        break
    if((exitCode < 3)or(exitCode > 7)and (exitCode != 0)):
        print("Failed to insert coins. Try to insert 3 - 7 coins at a time (0 ends).")
        continue
    else:
        totalCoin = totalCoin + exitCode


print("Thank you for using the program.")
