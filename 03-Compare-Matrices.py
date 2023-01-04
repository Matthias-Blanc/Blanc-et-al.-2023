def compare_matrices(matrix1, matrix2):
    # initialize a difference score to 0
    difference_score = 0
    
    # iterate through each element in the matrices
    for i in range(4):
        for j in range(4):
            # add the absolute difference between the elements to the difference score
            difference_score += abs(matrix1[i][j] - matrix2[i][j])
                
    # return the difference score as a percentage of the total possible difference
    # (which is the maximum possible difference for each element, since the elements are integers)
    return difference_score / (4 * 4 * max(matrix1[i][j], matrix2[i][j]))


difference_score = compare_matrices(matrix1, matrix2)
print(difference_score) 
