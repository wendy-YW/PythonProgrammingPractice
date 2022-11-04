#python week4_2


print("Let's figure out if character exists in the string")

string= input("Give string: ")
character= input("Give character: ")

result = string.find(character)

if(result != -1):
    print("Character "+"\'"+character+"\'","is in the string:","\'"+string+"\'.")
else:
    print("Character "+"\'"+character+"\'","doesn't exist in the string:","\'"+string+"\'.")

print("Let's figure out word's alphabetic order")

first= input("Give 1st word: ")
second=input("Give 2nd word: ")


if((first < second)==1):
    print("\'"+first+"\'","word is before the","\'"+second+"\'","word in alphabetic order.")
elif(first == second):
    print("Both words are the same, "+"\'"+first+"\'.")
else:
    print("\'"+second+"\'","word is before the","\'"+first+"\'","word in alphabetic order.")


print("Let's find out if the word is a palindrome.")

word=input("Give word: ")
 
if(word==word[::-1]) :
    print("Word is a palindrome.")
else:
    print("Word isn't a palindrome.")



print("Thank you for using the program.")
