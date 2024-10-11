import numpy as np

def menu(): # selecting a task
    while True:
        print(" Menu: ")
        print(" 1. Task 1 ")
        print(" 2. Task 2")
        print(" 0. Exit ")
        
        choice = input(" Select a task: ")
        
        if choice == '1':
            task1_proc10()
        elif choice == '2':
            task2_matrix3()
        elif choice == '0':
            print(" Exit!")
            break
        else: # error notification
            print(" Wrong choice. Please select again.")

def task1_proc10():
    print(" *** Task 1 Proc 10 ***")
    try:
        # enter values A, B, C, D
        A = float(input(" A = "))
        B = float(input(" B = "))
        C = float(input(" C = "))
        D = float(input(" D = "))
        # list of values
        val = [A, B, C, D]
        # processing function
        A, B, C, D = process_list(val)
        # new values A, B, C, D
        print(" New values:" ,  A, B, C, D )
    except ValueError:
        print(" All must be numbers!")

def Swap(X, Y):
    return Y, X

def process_list(val):
    # unpack the list of values
    A, B, C, D = val 
    # sequential replacement for pairs: A and B, C and D, B and C
    A, B = Swap(A, B)
    C, D = Swap(C, D)
    B, C = Swap(B, C)
    # return the updated numbers
    return A, B, C, D  
    
def task2_matrix3():
    print( " *** Task 2 Matrix 3 ***" )
    # name of the matrix file
    file_name = 'matrix.txt'
    # internal function
    row_sums, row_prods, transf_matrix = process_matrix(file_name)
    # output sum of elements of each row
    print(" Sums of elements of each row:")
    print(row_sums)
    # output product of elements of each row
    print(" Multiplication of the elements of each row:")
    print(row_prods)
    # output transformed matrix
    print(" Transformed matrix (matrix - random matrix):")
    print(transf_matrix)
    
def process_matrix(file_name):
    # download the matrix from the file
    matrix = np.loadtxt(file_name, delimiter=' ')
    # calculation of the sum and product of the elements of each row
    row_sums = np.sum(matrix, axis=1)
    row_prods = np.prod(matrix, axis=1)
    # create a matrix of the same size with random numbers
    random_matrix = np.random.random(matrix.shape)
    # calculate the difference between a given matrix and a random matrix
    transf_matrix = matrix - random_matrix
    return row_sums, row_prods, transf_matrix
    
menu()
