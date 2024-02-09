#Элизбаров Оганес, группа 37/1

#Задание 1
def sort(arr):
    size = len(arr)
    for i in (0, size-1):
        for j in range(i+1, size):
            if(arr[i]>arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def division_into_sets(arr1, arr2):
    Anya_Borya = set()
    for i in arr1:
        for j in arr2:
            if(i==j):
                Anya_Borya.add(i)
                continue
    Anya = set(x for x in arr1 if x not in Anya_Borya)
    Borya = set(x for x in arr2 if x not in Anya_Borya)
    return  [Anya_Borya, Anya, Borya]

N_M = input().split()
N = int(N_M[0])
M = int(N_M[1])
Anya = set()
Borya = set()
for i in range(0, N):
    Anya.add(int(input()))
for i in range(0, M):
    Borya.add(int(input()))
result = division_into_sets(Anya, Borya)
print(len(result[0]),"\n", result[0], "\n",len(result[1]),"\n", result[1], "\n",len(result[2]),"\n", result[2], "\n")
