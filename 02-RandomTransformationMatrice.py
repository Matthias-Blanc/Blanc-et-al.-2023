import random

def generate_random_matrix():
    # Initialize an empty 4x4 matrix
    matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]

    # Fill the matrix with random values between -1 and 1
    for i in range(3):
        for j in range(4):
            matrix[i][j] = random.uniform(-5, 5)

    return matrix

# Generate a random 4x4 matrix
matrix = generate_random_matrix()
print(matrix)
# Print the matrix
for row in matrix:
    print(row)
