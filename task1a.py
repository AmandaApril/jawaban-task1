def print_triangle_pattern_a(rows):
    for i in range(1, rows + 1):
        print('* ' * i)

def print_triangle_pattern_b(rows):
    for i in range(rows, 0, -1):
        print('* ' * i)

def print_triangle_pattern_c(rows):
    for i in range(rows, 0, -1):
        for j in range(1, i):
            print(" ", end=" ")
        for k in range(i, rows + 1):
            print("*", end=" ")
        print()

def print_triangle_pattern_d(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '* ' * i)

# Test the functions with different number of rows
print("Triangle Pattern A:")
print_triangle_pattern_a(5)

print("\nTriangle Pattern B:")
print_triangle_pattern_b(5)

print("\nTriangle Pattern C:")
print_triangle_pattern_c(5)

print("\nTriangle Pattern D:")
print_triangle_pattern_d(5)
