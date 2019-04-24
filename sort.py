import time

def insert_sort(A):
    """
    Сортировка вставками
    """
    N=len(A)
    for pop in range(N):
        k = pop-1
        while k>-1 and A[k]>A[k+1]:
            A[k],A[k+1] = A[k+1],A[k]
            k-=1

def bubble_sort(A):
    """
    Сортировка пузырьком
    """
    changed = True
    while changed:
        changed = False
        for i in range(len(A) - 1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                changed = True

def sel_sort(A):
    """
    Сортировка выбором
    """
    for i in range(len(A) - 1):
        m = i
        j = i + 1
        while j < len(A):
            if A[j] < A[m]:
                m = j
            j = j + 1
        A[i], A[m] = A[m], A[i]


def test_sort(sort_algorithm):
    print('test #1')
    A=[5,4,3,2,1]
    A_sorted=[1,2,3,4,5]
    sort_algorithm(A)
    print("OK" if A==A_sorted else "Fail")

    print('test #2')
    A=[4,4,4,4,4]
    A_sorted=[4,4,4,4,4]
    sort_algorithm(A)
    print("OK" if A==A_sorted else "Fail")


    print('test #3')
    start1 = time.time()
    A=[1,4,5,3,6,8,3,4,7]
    A_sorted=[1,3,3,4,4,5,6,7,8]
    sort_algorithm(A)
    end1 = time.time()
    print("OK" if A==A_sorted else "Fail", 'time: ',end1 - start1)


print(test_sort(insert_sort))

print(test_sort(bubble_sort))

print(test_sort(sel_sort))
