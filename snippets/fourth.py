t = raw_input()
t = int(t)

for i in range(1, t + 1):

    N, K, M = raw_input().split(" ")
    N = int(N)
    K = int(K)
    M = int(M)

    list1 = list()
    list2 = list()

    for j in range(0, N):
        string2 = raw_input('')
        list1.append(string2)
        count = 0
        string1 = ""
        for ele in list1[j]:
            if count < M:
                string1 += ele
            else:
                break
            count += 1
        list2.append(string1)

    print list2
    dict1 = dict()
    for j in range(0, N):
        dict1[list1[j]] = list2[j]
    list3 = sorted([(value, key) for (key, value) in dict1.items()])
    for k in range(0, K):
        if k == (K - 1):
            print(list3[k][1])
