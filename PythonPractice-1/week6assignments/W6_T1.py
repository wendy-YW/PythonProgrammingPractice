#python week6_1



def outputInstructions():
    print("This program asks filename and extension. Then outputs filename with extension.")
    print("Give first filename and then the file extension without a dot.")
    print("\nThis subprogram asks user input.")
    return None
    
def askQuestion(prompt):
    file_name = input("Give filename: ")
    print("This subprogram asks user input.")
    file_extention = input("Give file extension: ")
    prompt = file_name+"."+file_extention
    return prompt

def outputResults(result):
    print("This subprogram prints filename with the file extension.")
    print("Filename: "+result)
    return None


def main():
    outputInstructions()
    tem_result = askQuestion(0)
    outputResults(tem_result)
    print("\nThank you for using the program.")
    return None


main()



