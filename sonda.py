from z3 import *

random_values = [1227918265, 3978157, 263514239, 1969574147, 1833982879,
                 488658959, 231688945, 1043863911, 1421669753, 1942003127,
                 1343955001, 461983965, 602354579, 726141576, 1746455982,
                 1641023978, 1153484208, 945487677, 1559964282, 1484758023]
initial_seed = 17

solver = Solver()

flags = [BitVec(f"flag{i}", 8) for i in range(initial_seed)]
pointers = [BitVec(f"pointer{i}", 32) for i in range(initial_seed)]

solver.add(pointers[0] == 2 * initial_seed + random_values[0] % (5 * initial_seed))

for i in range(1, initial_seed):
    previous_pointer = pointers[i - 1]
    solver.add(pointers[i] == previous_pointer + random_values[i] % 94 + 33)

for j in range(initial_seed):
    sum_flag = BitVecVal(0, 32)
    for k in range(j + 1):
        sum_flag += ZeroExt(24, flags[k])
    solver.add(pointers[j] == sum_flag)

print(solver.check())
model = solver.model()
print(model)