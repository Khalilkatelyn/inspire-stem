#this is a programme to show palindromr strings
#date : 23/02/2024
#name : kate

word = str(input("enter the word"))
new_word = word [ ::-1]
print("the reverse is" , new_word)

if (new_word == word) :
    print("this is a palindrome word")
