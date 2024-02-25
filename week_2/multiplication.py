#this is a programme that prints the multiplication table
#date : 23/02/2024
#name :kahlil

num =input("the multiplication table of")
for n in range ( 1 , 11) :
    print(num, 'x', n, '=',num * n)

#full set
#multiplication table consisting 1 - 9
    
for column in range (1 - 10) :
    for rows in range (1 - 10) :
        print(rows * column , end = '\t')
        
