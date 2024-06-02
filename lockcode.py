from z3 import *

solver = Solver()

digits = [Int(f'digit_{i}') for i in range(3)]
for d in digits:
    solver.add(d >= 0, d <= 9)

    # One number is correctl and well placed

solver.add(Sum([If(digits[i] == 2, 1, 0) for i in range(3)]) +
           Sum([If(digits[i] == 9, 1, 0) for i in range(3)]) +
           Sum([If(digits[i] == 1, 1, 0) for i in range(3)]) == 1)
solver.add(Or(digits[0] == 2, digits[1] == 9, digits[2] == 1))

# One number is correct but wrong placed

solver.add(Sum([If(digits[i] == 2, 1, 0) for i in range(3)]) +
           Sum([If(digits[i] == 4, 1, 0) for i in range(3)]) +
           Sum([If(digits[i] == 5, 1, 0) for i in range(3)]) == 1)
solver.add(And(digits[0] != 2, digits[1] != 4, digits[2] != 5))

# Well two numbers are correct but wrong placed

solver.add(Sum([If(digits[i] == 4, 1, 0) for i in range(3)]) +
           Sum([If(digits[i] == 6, 1, 0) for i in range(3)]) +
           Sum([If(digits[i] == 3, 1, 0) for i in range(3)]) == 2)
solver.add(And(digits[0] != 4, digits[1] != 6, digits[2] != 3))

# Nothing is correct 

solver.add(And(digits[0] != 5, digits[1] != 5, digits[2] != 5))
solver.add(And(digits[0] != 7, digits[1] != 7, digits[2] != 7))
solver.add(And(digits[0] != 8, digits[1] != 8, digits[2] != 8))

# A number is correct but wrong placed

solver.add(Sum([If(digits[i] == 5, 1, 0) for i in range(3)]) +
           Sum([If(digits[i] == 6, 1, 0) for i in range(3)]) +
           Sum([If(digits[i] == 9, 1, 0) for i in range(3)]) == 1)
solver.add(And(digits[0] != 5, digits[1] != 6, digits[2] != 9))

if solver.check() == sat:
    model = solver.model()
    solution = [model[digits[i]].as_long() for i in range(3)]
else:
    solution = None

print(solution)

# Honestly this was a good one to learn
