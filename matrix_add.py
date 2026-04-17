rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

def get_matrix(name):
    print(f"Enter elements for Matrix {name}:")
    return [[int(input(f"Element [{r}][{c}]: ")) for c in range(cols)] for r in range(rows)]

matrix_a = get_matrix("A")
matrix_b = get_matrix("B")

result = [[matrix_a[i][j] + matrix_b[i][j] for j in range(cols)] for i in range(rows)]

print("\nResultant Matrix:")
for row in result:
    print(row)
