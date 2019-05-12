def max_growing_subseq(numb_arr):
    n = len(numb_arr)
    d = [1]*n
    prev = [-1]*n
    for i in range(n):
        for j in range(i):
            if numb_arr[i]>numb_arr[j] and d[i]<d[j]+1:
                d[i] = d[j] + 1
                prev[i] = j
    print(d)
    print(max(d), d.index(max(d)))
    print(prev)

test_arr = [1,3,2,3,5]
max_growing_subseq(test_arr)
