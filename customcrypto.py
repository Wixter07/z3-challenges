from z3 import *

# Read encrypted values from file
with open("enc.txt", "r") as file:
    content = file.read().strip()
    content = content.replace('[', '').replace(']', '')
    encrypted_values = list(map(int, content.split(',')))


known = 'pwned'
solver = Solver()

enc = [BitVec(f"enc_{i:02}", 8) for i in range(len(encrypted_values))]
dec = [BitVec(f"dec_{i:02}", 8) for i in range(len(encrypted_values))]
key = [BitVec(f"key_{i:02}", 8) for i in range(4)]


for i, char in enumerate(known):
    solver.add(dec[i] == ord(char))

for i in range(len(encrypted_values)):
    chunk = i // 4
    offset = i % 4
    solver.add(enc[i] == encrypted_values[i])
    solver.add((dec[i] + chunk) ^ key[offset] == enc[i])
    solver.add(dec[i] >= 32, dec[i] <= 126)

if solver.check() == sat:
    model = solver.model()
    flag = ''.join(chr(model[dec[i]].as_long()) for i in range(len(encrypted_values)))
    print(f"Flag: {flag}")
else:
    print("Ghey")
