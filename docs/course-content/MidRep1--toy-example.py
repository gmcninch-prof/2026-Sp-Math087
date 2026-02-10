"""
Toy Example: Simple Transportation Problem.

Optimal widget shipping from 2 factories to 3 stores
"""

################################################################################
## create the network flow diagram
################################################################################

from graphviz import Digraph

# Create a new directed graph
dot = Digraph(comment='Toy Example Network Flow')
dot.attr(rankdir='LR')  # Left to right layout

# Define node styles
dot.attr('node', shape='circle', style='filled', fillcolor='lightblue')

# Add nodes
# Source and terminal with different color
dot.node('Source', 'Source', fillcolor='lightgreen')
dot.node('Terminal', 'Terminal', fillcolor='lightcoral')

# Factory nodes
dot.node('FA', 'Factory A', fillcolor='lightyellow')
dot.node('FB', 'Factory B', fillcolor='lightyellow')

# Store nodes
dot.node('S1', 'Store 1', fillcolor='lightblue')
dot.node('S2', 'Store 2', fillcolor='lightblue')
dot.node('S3', 'Store 3', fillcolor='lightblue')

# Add edges from source to factories (with supply capacities)
dot.edge('Source', 'FA', label='supply≤100')
dot.edge('Source', 'FB', label='supply≤80')

# Add edges from factories to stores (with shipping costs)
dot.edge('FA', 'S1', label='cost=$2')
dot.edge('FA', 'S2', label='cost=$3')
dot.edge('FA', 'S3', label='cost=$5')
dot.edge('FB', 'S1', label='cost=$4')
dot.edge('FB', 'S2', label='cost=$2')
dot.edge('FB', 'S3', label='cost=$3')

# Add edges from stores to terminal (with demands)
dot.edge('S1', 'Terminal', label='demand=60')
dot.edge('S2', 'Terminal', label='demand=70')
dot.edge('S3', 'Terminal', label='demand=50')

# Save the diagram
filename = "MidRep1--2025-02-16--toy-network-diagram"
dot.render(filename, format='png', cleanup=True)
print(f"Network diagram saved on disk as\n '{filename}.png'")

################################################################################
## create and use the linear program 
################################################################################

import numpy as np
from scipy.optimize import linprog

# Define the problem data
# Shipping costs (dollars per widget): rows = factories, cols = stores
costs = np.array([
    [2, 3, 5],  # Factory A to Stores 1, 2, 3
    [4, 2, 3]   # Factory B to Stores 1, 2, 3
])

# Flatten cost matrix for objective function
#   (order: A1, A2, A3, B1, B2, B3)
c = costs.flatten()

# Supply capacities
supply = np.array([100, 80])  # Factory A, Factory B

# Store demands
demand = np.array([60, 70, 50])  # Store 1, Store 2, Store 3

# Build constraint matrices
# Supply constraints (inequality): sum over stores <= supply
A_supply = np.array([
    [1, 1, 1, 0, 0, 0],  # Factory A
    [0, 0, 0, 1, 1, 1]   # Factory B
])
b_supply = supply

# Demand constraints (equality): sum over factories = demand
A_demand = np.array([
    [1, 0, 0, 1, 0, 0],  # Store 1
    [0, 1, 0, 0, 1, 0],  # Store 2
    [0, 0, 1, 0, 0, 1]   # Store 3
])
b_demand = demand

# Solve the linear program
result = linprog(
    c=c,
    A_ub=A_supply,
    b_ub=b_supply,
    A_eq=A_demand,
    b_eq=b_demand
)  
# Display results
if result.success:
    print("Optimal shipping cost: $%.2f" % result.fun)
    print("\nOptimal shipping plan:")
    print("Factory A -> Store 1: %.1f widgets" % result.x[0])
    print("Factory A -> Store 2: %.1f widgets" % result.x[1])
    print("Factory A -> Store 3: %.1f widgets" % result.x[2])
    print("Factory B -> Store 1: %.1f widgets" % result.x[3])
    print("Factory B -> Store 2: %.1f widgets" % result.x[4])
    print("Factory B -> Store 3: %.1f widgets" % result.x[5])
    
    # Reshape for display as matrix
    shipping_matrix = result.x.reshape(2, 3)
    print("\nShipping matrix:")
    print(shipping_matrix)
else:
    print("Optimization failed:", result.message)
    
