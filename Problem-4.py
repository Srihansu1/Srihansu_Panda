numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
multiple_count={}
for i in range(1,10):
    count = 0
    for j in numbers:
        if j%i ==0:
            count = count+1
    multiple_count[i]=count
print(multiple_count)

