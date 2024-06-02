from z3 import *

solver = Solver()

password = [BitVec(f"pwd{i}", 8) for i in range(48)]

license_key = bytearray(bytes.fromhex("04b2fc467e104c0c610e3bf0a009a9f3621905df1997ce0b6cd6a3ea68af4d4deaaf024906f7b259ba32035ac4dad586"))
key = [int(x) for x in license_key]
v5 = [BitVec(f"key{i}", 8) for i in range(48)]


for i in range(len(key)):
    solver.add(v5[i] == key[i])

# The constraints derived from Ghidra
v4 = 0
for i in range(12):
    solver.add(v5[v4] == 33 * password[v4 + 3] + 89 * password[v4 + 2] + 103 * password[v4 + 1] + 66 * password[v4])
    solver.add(v5[v4 + 1] == 73 * password[v4] + -125 * password[v4 + 1] + -103 * password[v4 + 2] + 51 * password[v4 + 3])
    solver.add(v5[v4 + 2] == 113 * password[v4 + 1] + password[v4 + 3] + 54 * password[v4] + 8 * password[v4 + 2])
    solver.add(v5[v4 + 3] == 25 * password[v4 + 2] + 23 * password[v4 + 3] + 119 * password[v4] + 3 * password[v4 + 1])
    v4 += 4

# ASCII RANGE SET
for i in range(48):
    solver.add(password[i] >= 32)
    solver.add(password[i] <= 126)

if solver.check() == sat:
    model = solver.model()
    flag = ''.join(chr(model[p].as_long()) for p in password)
    print(flag)

else:
    print("Ghey")

