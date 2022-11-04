#python week4_5


print("This is a menu driven program, where you can choose which operation the program performs.")
print("Choose the operation below:")
print("1) Grams to pounds")
print("2) Length conversions")
print("0) Exit")

option1= input("Give option: ")

if(option1.isdigit()):
    option=int(option1)
    if(option==1):
        grams= float(input("Give grams: "))
        print("Weight in pounds:",grams*0.002205)
    elif(option==2):
        print("Select units from list: ")
        print("1) Millimeters")
        print("2) Meters")
        print("3) Kilometers")
        
        source_unit=int(input("Source unit(1-3): "))
        target_unit=int(input("Target unit(1-3): "))
        value_unit=""
        if(target_unit==1):
            value_unit="mm"
        elif(target_unit==2):
            value_unit="m"
        elif(target_unit==3):
            value_unit="km"

        length=float(input("Give length: "))
        

        if(source_unit==1):
            if(target_unit==2):
                length=length*0.001
            elif(target_unit==3):
                length=length*0.000001
        elif(source_unit==2):
            if(target_unit==1):
                length=length*1000
            elif(taget_unit==3):
                length=length*0.001
        elif(source_unit==3):
            if(target_unit==1):
                length=length*1000000
            elif(taget_unit==2):
                length=length*1000
                
        print("Converted value:",length,value_unit)
        
    elif(option==0):
        print("Exiting!")
    else:
        print("Unknown option.")
        
else:
    print("Unknown option.")


print("Thank you for using the program.")
