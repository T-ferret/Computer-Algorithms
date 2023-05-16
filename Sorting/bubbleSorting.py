def bubble_sort(seq):
    length = len(seq)-1
    tmp = list(seq)

    for num in range(length, 0, -1):
        tmp2 = list(tmp)
        for i in range(num):
            if tmp[i] > tmp[i+1]:
                tmp[i], tmp[i+1] = tmp[i+1], tmp[i]
        if tmp == tmp2:
            break
    return tmp
        
def bubble_down_sort(seq):
    length = len(seq)-1
    tmp = list(seq)
    for num in range(length, 0, -1):
        tmp2 = list(tmp)
        for i in range(num):
            if tmp[i] < tmp[i+1]:
                tmp[i], tmp[i+1] = tmp[i+1], tmp[i]
        # print(seq)
        if tmp == tmp2:
            break
    return tmp

def bubble_swap_sort(seq):
    length = len(seq)-1
    tmp = list(seq)

    for num in range(length, 0, -1):
        swap = False
        for i in range(num):
            if tmp[i] > tmp[i+1]:
                tmp[i], tmp[i+1] = tmp[i+1], tmp[i]
                swap = True
        if not swap:
            break
    return tmp

def bubble_swap_down_sort(seq):
    length = len(seq)-1
    tmp = list(seq)

    for num in range(length, 0, -1):
        swap = False
        for i in range(num):
            if tmp[i] < tmp[i+1]:
                tmp[i], tmp[i+1] = tmp[i+1], tmp[i]
                swap = True
        if not swap:
            break
    return tmp

def test_bubble_sort():
    seq = [4, 5, 2, 1, 6, 2, 7, 10, 13, 8]
    seq2 = []

    for i in range(10, 0, -1):
        seq2.append(i)

    SortedSeq = bubble_sort(seq)
    print(f"seq 오름차순 정렬 : {seq} -> {SortedSeq}")
    print()

    SortedDownSeq = bubble_down_sort(seq)
    print(f"seq 내림차순 정렬 : {seq} -> {SortedDownSeq}")
    print()

    SortedSeq2 = bubble_swap_sort(seq2)
    print(f"seq2 오름차순 정렬 : {seq2} -> {SortedSeq2}")
    print()

test_bubble_sort()