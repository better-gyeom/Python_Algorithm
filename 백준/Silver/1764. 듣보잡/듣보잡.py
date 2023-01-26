N, M = input().split()
N = int(N)
M = int(M)

notlisten = set()
notsee = set()

for _ in range(N):
    n = input()
    notlisten.add(n)

for _ in range(M):
    m = input()
    notsee.add(m)

not_listen_and_see = sorted(list(notlisten & notsee))
print(len(not_listen_and_see), *not_listen_and_see, sep='\n')
