limit = int(input("Enter your limit : "))
arr=list(map(int,input("ENter your numbers: ").split()[:limit]))
largest = max(arr)

for i in range(limit):
    if largest == max(arr):
        arr.remove(max(arr))

print(max(arr))