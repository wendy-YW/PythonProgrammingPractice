#python week5_5


start_value = int(input("Give starting point: "))
end_value = int(input("Give stopping point: "))
inspection_value = int(input("Give inspection point: "))

if(inspection_value<start_value or inspection_value> end_value ):
    print("\nInspection has to be within the range.")
    print("Thank you for using the program.")
else:
    print("\nFirst loop:")
    for i in range(start_value,inspection_value):
        print(str(i), end=' ')
    print(inspection_value)

    print("\nSecond loop:")
    j = start_value
    while j < end_value:
        if(j == inspection_value):
            j+=1
            continue
        print(j,end=' ')
        j += 1

    print(end_value)
    
    print("\nThank you for using the program.")
