#python week4_3


print("Let's figure out product sale percentage and selling price.")

price= float(input("What is the product's list price: "))


print("How should we count the new sale price?")
print("1) In one multi-branched selection structure")
print("2) In multiple separate selection structures")

option1= int(input("Give option: "))

if(option1==1 or option1 ==2):
    option = option1
else:
    print("Unknown option.")
    quit() 

saleP = 0 
if(option !=1):
    print("With multiple separate selection structures the results are following:")
    if(price>=500):
        saleP=50
        price=price*0.5
    if(price>=150):
        saleP=25
        price=price*0.75
    if(price>=0):
        saleP=10
        price=price*0.9
else:
    print("With one multibranched selection structure the results are following:")
    if(price>=500):
        saleP=50
        price=price*0.5
    elif(price>=150):
        saleP=25
        price=price*0.75
    else:
        saleP=10
        price=price*0.9


if(option==2):
    print("Product price reduction is",str(saleP)+"%"+" and the remaining price is",str(round(price,2))+"e.")
else:
    print("Product sale percentage is",str(saleP)+"%"+" and the remaining price is",str(round(price,2))+"e.")
    

print("Thank you for using the program.")
