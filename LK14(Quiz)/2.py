K, M = input().split(" ")
K = int(K)
M = int(M)
i = 0
S = 0
z = []

while i < K:
    N = int(input("Input N : "))
    ii = 0
    s = 0
    while ii < N:
        f = int(input("Input I : "))
        if f > s:
            s = f
        ii += 1
    z.append(s)
    i +=1 

for x in z:
        S = S + x**2
print(z)
S = S % M
print(S)
