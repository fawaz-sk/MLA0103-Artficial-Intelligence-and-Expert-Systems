jug1 = 11
jug2 = 9

a = 0
b = 0

print("Initial:", a, b)

a = 11
print("Fill Jug1:", a, b)

transfer = min(a, jug2 - b)
a -= transfer
b += transfer
print("Pour Jug1 -> Jug2:", a, b)

b = 0
print("Empty Jug2:", a, b)

transfer = min(a, jug2 - b)
a -= transfer
b += transfer
print("Pour Jug1 -> Jug2:", a, b)

a = jug1
print("Fill Jug1:", a, b)

transfer = min(a, jug2 - b)
a -= transfer
b += transfer
print("Pour Jug1 -> Jug2:", a, b)

b = 0
print("Empty Jug2:", a, b)

transfer = min(a, jug2 - b)
a -= transfer
b += transfer
print("Pour Jug1 -> Jug2:", a, b)

a = jug1
print("Fill Jug1:", a, b)

transfer = min(a, jug2 - b)
a -= transfer
b += transfer
print("Pour Jug1 -> Jug2:", a, b)

if a == 8:
    print("Target Achieved: 8", b)
