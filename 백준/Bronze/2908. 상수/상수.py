A, B = input().split()

Ai = int(A[::-1])
Bi = int(B[::-1])

print(Ai if Ai > Bi else Bi)