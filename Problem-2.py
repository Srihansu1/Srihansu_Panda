a = int(input())
for i in range(a):
    if i == a - 1:
        print(2*i + 1, end="")
    else:
        print(2*i + 1, end=", ")
