#python week5_4 


print("Program asks for strings and finds the longest string.")

prompted_strings = int(input("How many strings are prompted: "))

shortest_string = int(input("Shortest string (in characters) allowed: "))

prompted_start=0
temp_word_length=0

while (prompted_start<prompted_strings) :
        prompted_start+=1
        word = input("Give a word: ")
        if(len(word)>=shortest_string):
            if(temp_word_length<len(word)):
                longest_word = word
        else:
            print("Program ends, because the inserted string was too short.")
            break

if(prompted_start == prompted_strings):
   print("Program ends because all the strings were prompted.")
           
print("You gave",str(prompted_start),"strings.")
print("Longest string was \'"+longest_word+"\', which had",str(len(longest_word)),"characters.")

print("Thank you for using the program.")
