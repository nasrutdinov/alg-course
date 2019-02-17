def insert_sort(A):
    N=len(A)
    for top in range(1,N):
        k=top
        while k>0 and A[k-1]>A[k]:
            A[k],A[k-1]= A[k-1], A[k]
            k=k-1


def test_sort(sort_algorithm):
    print("test # 1")
    A=[5,4,3,2,1]
    A_sorted=[1,2,3,4,5]
    sort_algorithm(A)
    print("Ok" if A==A_sorted else "Fail")
    #test 2
    print("test # 2")
    A = [6, 4, 4, 2, 2]
    A_sorted = [2, 2, 4, 4, 6]
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")
    #test 3
    print("test # 3")
    A = list(range(10,20)) + list(range(1,10))
    A_sorted = list(range(1,20))
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")

test_sort(insert_sort)
