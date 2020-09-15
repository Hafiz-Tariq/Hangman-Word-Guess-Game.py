#qt5 module and database if want to is embeded in it otherwise it is very okay
#Hangman Project starts with covering Qt5 module &&& sqlite3 ultimately!!!

# from time import sleep
#
# previous_guess = 'NULL'
# find=0
#
# print("Starting a new Game!!!")
#
# #Incorrect attempts counting!!!
# while True:
#     try:
#         incorrect_attempts = int(input("How many Incorrect attempts you want(1-10) ??? - "))
#         if (incorrect_attempts<1 or incorrect_attempts>10)  :
#             print("Limit is exceeded or Lessen. Try again!")
#         else:
#             break
#     except ValueError:
#         print("Invalid Input --- Only integers entered!!!")
# # ////////
#
# # #Minimum Words Length if you using your own dictionary
# while True:
#     try:
#         minimum_length=int(input("Choose the word Length (5-14) : "))
#         if (minimum_length<5 or minimum_length>14)  :
#             print("Limit is exceeded or Lessen. Try again!")
#         else:
#             break
#     except ValueError:
#         print("Invalid Input --- Only integers entered!!!")
# # ////////
#
# #fetch word through file Handling from raw_string.txt
# i=0
# file = open('raw_strings.txt','r')
# word = file.readlines()
# for i in range(0, len(word)):
#     if (len(word[i]) - 1) == minimum_length:
#         break
# string = word[i].strip('\n')  #defining word which will be guess
# file.close()
# #/////////////////
# asterick = len(string) * '*'
# ###proper Game starts from here !!!
# #............................
# pre_guess_list = []
# print('\n\n\t\t Selecting a word from dictionary ... ') , sleep(1)
#
# while True:
#     #showing the astericks as a word and unhide each letter by correct guess
#     asterick = str(''.join(asterick))
#     if asterick.strip()==string.strip():
#         print("Word is : " , string,'You Win~Enjoy!!!' )
#         break
#     print('\n\tWord is : ' , end='')
#     print(asterick)
#     asterick = list(asterick)
#     #////////////
#     print('\tPrevious Guess : ' , previous_guess)
#     #Attempts Calculation
#     if incorrect_attempts>0:
#         print("\tAttempts Remaining : " , incorrect_attempts)
#     else:
#         print("Incorrect attempts are ended.Sorry!!!")
#         print("The correct word is : " , string , "\nAnd you guess : " , str(''.join(asterick)))
#         break
#     #//////
#
#     #Checking the limit of a string ...
#     while True:
#         try:
#             check_in_string=input("\tChoose a letter : " )
#             if (len(check_in_string) != 1)  :
#                 print("Limit is exceeded from letter to string. Try again!")
#             elif check_in_string==previous_guess :
#                 print("Please Try again.You already Guess ",previous_guess)
#             else:
#                 break
#         except ValueError:
#             print("Invalid Input --- Only String entered!!!")
#     #////
#     #checking letter in giving string...
#     previous_guess = check_in_string
#     pre_guess_list.append(previous_guess)
#     find = 0
#     # There is some extra load here check to optimize it!!!
#     for find in range(len(string)):
#         if string[find] == check_in_string :
#             #checking any duplicate letter in string (optional)
#             for check in range(find,len(string)):
#                 if string[check] == check_in_string:
#                     asterick[check] = check_in_string.strip()
#                     continue
#             break
#     else:
#         for guess in range(len(pre_guess_list)):
#             if pre_guess_list[guess] != check_in_string:
#                 continue
#             else:
#                 print(check_in_string ," is not in the word.")
#                 incorrect_attempts-=1
#                 break
#     #////
#
#
#
# #Delte the word from file -raw_string.txt-  after user played with it !!!
# temp_file = open('raw_strings.txt', 'w' )
# for temp in word:
#     if temp.strip('\n') != word[i].strip('\n'):
#         temp_file.write(temp)
# temp_file.close()
# # ////////
import sqlite3 as sql
con = sql.connect('MyWords.db')
cobj = con.cursor()



file = open('Words.txt','r')
words = file.readlines()

# def insert_values(idd,a1,b2,c3,d4,e5,f6,g7,h8,i9,j10,k11,l12,m13,n14,o15,p16,q17,r18,s19,t20,u21,v22,w23,x24,y25,z26):
#     cobj.execute('INSERT INTO Unsorted_words VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)' ,
#                       (idd,a1,b2,c3,d4,e5,f6,g7,h8,i9,j10,k11,l12,m13,n14,o15,p16,q17,r18,s19,t20,u21,v22,w23,x24,y25,z26))
#     con.commit()


a=''
b=''
c=''
d=''
e=''
f=''
g=''
h=''
i=''
j=''
k=''
l=''
m=''
n=''
o=''
p=''
q=''
r=''
s=''
t=''
u=''
v=''
w=''
x=''
y=''
z=''
# for check in words:

#
# for check in words:
#     if check[0]=='a':
#         a.append(check)
#     elif check[0]=='b':
#         b.append(check)
#     elif check[0] == 'c':
#         c.append(check)
#     elif check[0]=='d':
#         d.append(check)
#     elif check[0]=='e':
#         e.append(check)
#     elif check[0]=='f':
#         f.append(check)
#     if check[0]=='g':
#         g.append(check)
#     if check[0]=='h':
#         h.append(check)
#     elif check[0]=='i':
#         i.append(check)
#     elif check[0]=='j':
#         j.append(check)
#     elif check[0]=='k':
#         k.append(check)
#     elif check[0]=='l':
#         l.append(check)
#     elif check[0]=='m':
#         m.append(check)
#     elif check[0]=='n':
#         n.append(check)
#     elif check[0]=='o':
#         o.append(check)
#     elif check[0]=='p':
#         p.append(check)
#     elif check[0]=='q':
#         q.append(check)
#     elif check[0]=='r':
#         r.append(check)
#     elif check[0]=='s':
#         s.append(check)
#     elif check[0]=='t':
#         t.append(check)
#     elif check[0]=='u':
#         u.append(check)
#     elif check[0]=='v':
#         v.append(check)
#     elif check[0]=='w':
#         w.append(check)
#     elif check[0]=='x':
#         x.append(check)
#     elif check[0]=='y':
#         y.append(check)
#     elif check[0]=='z':
#         z.append(check)

# print(a[0],b[0],c[0],d[0],e[0],f[0],g[0],h[0],i[0],j[0],k[0],l[0],m[0],n[0],o[0],p[0],q[0],r[0],s[0],t[0],u[0],v[0],w[0],x[0],y[0],z[0])
# insert_values(0,a[0],b[0],c[0],d[0],e[0],f[0],g[0],h[0],i[0],j[0],k[0],l[0],m[0],n[0],o[0],p[0],q[0],r[0],s[0],t[0],u[0],v[0],w[0],x[0],y[0],z[0])
# print(x[500])

file.close()
cobj.close()
con.close()
