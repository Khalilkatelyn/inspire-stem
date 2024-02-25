#this is a programme to show the pascal's triangle
#date :23/02/2024
#name :kate

def generate_pascals_triangle(rows):
    return triangle 

def print_pascals_triangle(triangle):
    for row in triangle:
        print(" ".join(str(num) for num in row).center(len(triangle) * 2))

rows = 5
triangle = generate_pascals_triangle(rows)
print_pascals_triangle(triangle)
