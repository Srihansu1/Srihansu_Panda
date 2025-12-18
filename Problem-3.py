a = int(input("Enter a number: "))
s = []

if a <= 2:
    s = [1]
else:
    if a % 2 == 0:
        s_length = a + 1
    else:
        s_length = a
    s = [2*i + 1 for i in range(s_length)]

print(",".join(map(str, s)))

