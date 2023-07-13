lst = list(map(int, input().split()))
def Max_Min_Array(lst):
    min_ele = float('inf')
    max_ele = float('-inf')
    for ele in lst:
        if ele < min_ele:
            min_ele = ele
        if ele > max_ele:
            max_ele = ele
    return max_ele + min_ele
print(Max_Min_Array([-2, 1, -4, 5, 3]))
print(Max_Min_Array([1, 3, 4, 1]))
print(Max_Min_Array(lst))   
