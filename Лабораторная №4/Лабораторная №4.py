def Max(k, arr):
    m1 = 0
    m2 = 0
    mx = 0
    for i in range(2 * k, len(arr)):
        m1 = max(m1, arr[i - 2 * k])
        m2 = max(m2, m1 + arr[i - k])
        mx = max(mx, m2 + arr[i])
    return mx

file = open("27-166b.txt", "r")

N, K = file.readline().replace("\n", " ").split()[0:2]
N = int(N)
K = int(K)
arr = []
lines = file.readlines()
for i in lines:
    arr.append(int(i.replace("\n", " ")))

print(Max(K, arr))