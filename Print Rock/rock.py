n = int(input("Enter number of rocks: "))
arr = []

for i in range(n):
    x = int(input("Enter height of rock: "))
    arr.append(x) 

print("="*20)
mx = max(arr)
for i in range(mx):
    for j in range(n):
        h = arr[j]
        for k in range(2*h):
            if i < mx - h:
                print(" ", end="")
            else:
                t = i - (mx - h)
                if k == h-1-t:
                    print("/", end="")
                elif k == h+t:
                    print("\\", end="")
                else:
                    print(" ", end="")
    print()

print()

for i in range(mx):
    for j in range(n):
        for k in range(2*arr[j]):
            if i < arr[j] and i == k:
                print("\\", end="")
            elif i < arr[j] and i+k == 2*arr[j]-1:
                print("/", end="")
            else:
                print(" ", end="")
    print()

print("="*20)