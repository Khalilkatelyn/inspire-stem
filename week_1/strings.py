#srings in python
#date :22/02/2024
#name :kate

city = "nairobi"

print(city[0])#n
print(city[1])#a
print(city[2])#i
print(city[3])
print(city[4])
print(city[-1])
print(city[-2])#i

#converts to uppercase


print("\n\n")#prints a new line
print(city.upper())

name ="KATE"
print(name)
print(name.lower())#converts string to lower case

town ="  naiva sha  "

print(town)
print("\t")#new tab
print(town.strip())

f_name ="kate"
s_name ="mwangi"

full_name = f_name + s_name

print(full_name)


#replacing a character

fruit = "ooorange"

print(fruit.replace('o' ,'y'))

subject ="physical;sciences"

print(subject.split(":"))

age = 30
height =1.2

print("i am {0} years old and {1} meters tall" ,format(age),(height))

#printing a string

activity = "dancing"
print("my hobby is %s" %(activity))

#printng an integer

height = 1.23
print("my height is %5.3f" % (height))

age = 17
print("my age is %d" %(age))

name ="kate m"
print(len(name))

print(f"my full name is {name}")

school = "engineering"
course = "electrical"

print("i am studying {course}  in the school of{school}" .format(course ="medicine",school="human sciences"))







