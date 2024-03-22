import numpy as np
from scipy.optimize import linear_sum_assignment

def optimal_assignment(matrix):
    # Convert the matrix to numpy array
    cost_matrix = np.array(matrix)
    
    # Apply the Hungarian algorithm
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    
    # Construct the optimal assignment
    assignment = {}
    for machine, job in zip(row_ind, col_ind):
        assignment[machine] = job
    
    return assignment

# Example matrix of machines and jobs
matrix = [
    [10, 20, 10],
    [15, 25, 30],
    [20, 15, 25]
]

# Get the optimal assignment
optimal_assign = optimal_assignment(matrix)
print("Optimal assignment:")
for machine, job in optimal_assign.items():
    print(f"Machine {machine + 1} -> Job {job + 1}")