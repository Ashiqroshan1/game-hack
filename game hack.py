last_10_numbers = [ 3,6,3,7,0,5,4,6,3,7]
last_number = last_10_numbers[-1]

s = sum(last_10_numbers)

if last_number == 0:
    s += 0
elif last_number == 1:
    s += 1
elif last_number == 2:
    s += 3
elif last_number == 3:
    s += 6
elif last_number == 4:
    s += 10
elif last_number == 5:
    s += 15
elif last_number == 6:
    s += 21
elif last_number == 7:
    s += 28
elif last_number == 8:
    s += 36
elif last_number == 9:
    s += 45

while s > 9:
    s = sum(map(int, str(s)))

if s % 2 == 0:
    color = "red"
else:
    color = "green"

print("Follow AshiqRoshan")
print(".")
print("Sum:", s)
print("Color:", color)
print(".")
print("Create by AshiqRoshan")