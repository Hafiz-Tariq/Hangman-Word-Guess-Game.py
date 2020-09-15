#Hangman project OR Word Search Game
from time import sleep

previous_guess = 'NULL'
find=0

print("Starting a new Game!!!")

#Incorrect attempts counting!!!
while True:
    try:
        incorrect_attempts = int(input("How many Incorrect attempts you want(1-10) ??? - "))
        if (incorrect_attempts<1 or incorrect_attempts>10)  :
            print("Limit is exceeded or Lessen. Try again!")
        else:
            break
    except ValueError:
        print("Invalid Input --- Only integers entered!!!")
# ////////

# #Minimum Words Length if you using your own dictionary
while True:
    try:
        minimum_length=int(input("Choose the word Length (5-14) : "))
        if (minimum_length<5 or minimum_length>14)  :
            print("Limit is exceeded or Lessen. Try again!")
        else:
            break
    except ValueError:
        print("Invalid Input --- Only integers entered!!!")
# ////////

#fetch word through file Handling from raw_string.txt
i=0
file = open('raw_strings.txt','r')
word = file.readlines()
for i in range(0, len(word)):
    if (len(word[i]) - 1) == minimum_length:
        break
string = word[i].strip('\n')  #defining word which will be guess
file.close()
#/////////////////
asterick = len(string) * '*'
###proper Game starts from here !!!
#............................
pre_guess_list = []
print('\n\n\t\t Selecting a word from dictionary ... ') , sleep(1)

while True:
    #showing the astericks as a word and unhide each letter by correct guess
    asterick = str(''.join(asterick))
    if asterick.strip()==string.strip():
        print("Word is : " , string,'You Win~Enjoy!!!' )
        break
    print('\n\tWord is : ' , end='')
    print(asterick)
    asterick = list(asterick)
    #////////////
    print('\tPrevious Guess : ' , previous_guess)
    #Attempts Calculation
    if incorrect_attempts>0:
        print("\tAttempts Remaining : " , incorrect_attempts)
    else:
        print("Incorrect attempts are ended.Sorry!!!")
        print("The correct word is : " , string , "\nAnd you guess : " , str(''.join(asterick)))
        break
    #//////

    #Checking the limit of a string ...
    while True:
        try:
            check_in_string=input("\tChoose a letter : " )
            if (len(check_in_string) != 1)  :
                print("Limit is exceeded from letter to string. Try again!")
            elif check_in_string==previous_guess :
                print("Please Try again.You already Guess ",previous_guess)
            else:
                break
        except ValueError:
            print("Invalid Input --- Only String entered!!!")
    #////
    #checking letter in giving string...
    previous_guess = check_in_string
    pre_guess_list.append(previous_guess)
    find = 0
    # There is some extra load here check to optimize it!!!
    for find in range(len(string)):
        if string[find] == check_in_string :
            #checking any duplicate letter in string (optional)
            for check in range(find,len(string)):
                if string[check] == check_in_string:
                    asterick[check] = check_in_string.strip()
                    continue
            break
    else:
        for guess in range(len(pre_guess_list)):
            if pre_guess_list[guess] != check_in_string:
                continue
            else:
                print(check_in_string ," is not in the word.")
                incorrect_attempts-=1
                break
    #////



#Delte the word from file -raw_string.txt-  after user played with it !!!
temp_file = open('raw_strings.txt', 'w' )
for temp in word:
    if temp.strip('\n') != word[i].strip('\n'):
        temp_file.write(temp)
temp_file.close()
# ////////
