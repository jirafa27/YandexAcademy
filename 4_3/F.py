def merge_sort(lst):
    if len(lst) == 1:
        return lst
    left = merge_sort(lst[:len(lst) // 2])
    right = merge_sort(lst[len(lst) // 2:])
    res = []
    i = 0
    j = 0
    while True:
        if left[i] > right[j]:
            res.append(right[j])
            j += 1
        else:
            res.append(left[i])
            i += 1
        if i == len(left):
            res.extend(right[j:])
            break
        if j == len(right):
            res.extend(left[i:])
            break
    return res
    
print(merge_sort([3, 1, 2]))
