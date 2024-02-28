my_laptop = {"make" :"hp" ,"colour" :"grey" ,"weight" :"1.0", "year": "2022"}


print(my_laptop["make"])
print(my_laptop["colour"])
print(my_laptop["year"])

#changes the value in a dictionary
my_laptop["colour"] = "red"
my_laptop["year"] = "2001"


print(my_laptop)


my_laptop["size"] = "1200mm x 600mm"
print(my_laptop)

del my_laptop ["colour"]
print(my_laptop)

"""
for key,value in my_laptop.items() :
    print(key)
    print("\n")
    print(value)
"""
