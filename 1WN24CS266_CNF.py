
from sympy import symbols
from sympy.logic.boolalg import to_cnf

# Define variables
P, Q, R = symbols('P Q R')

# Input expression
expr = (P >> Q) & (Q >> R)

print("Original Expression:", expr)

# Convert into CNF
cnf = to_cnf(expr, simplify=True)

print("CNF Expression:", cnf)
