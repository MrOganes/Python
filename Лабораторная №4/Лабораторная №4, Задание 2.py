file = open("27-166a.txt", "r")

arr = []
lines = file.readline().split()
for i in lines:
    arr.append(int(i))
print(arr)

kol = 0
for i in range(0, len(arr)-1):
    for j in range(i+1, len(arr)):
        if(arr[i]==arr[j]):
            kol+=1
        else:
            break
print(kol)

