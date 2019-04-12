"""
    // 二分查找法,在有序数组arr中,查找target
    // 如果找到target,返回相应的索引index
    // 如果没有找到target,返回None
"""


def binary_search_core(lst, left, right, target):
    index = None
    if right - left == 1:
        if lst[left] == target:
            return left
        else:
            return None
    mid = left + (right - left) // 2
    if target == lst[mid]:
        index = mid
    elif target < lst[mid]:
        index = binary_search_core(lst, left, mid, target)
    elif target > lst[mid]:
        index = binary_search_core(lst, mid + 1, right, target)
    return index


def binary_search_core_2(lst, left, right, target):
    while left < right:
        mid = left + (right - left) // 2
        if target == lst[mid]:
            return mid
        elif target < lst[mid]:
            right = mid
        elif target > lst[mid]:
            left = mid + 1
    return None


def binary_search(lst, target):
    if len(lst) <= 0:
        return None
    index = binary_search_core_2(lst, 0, len(lst), target)
    return index


if __name__ == '__main__':
    # data = [1, 3, 4, 5, 6, 8, 9, 13, 14, 15, 16]
    # data = [16]
    data = []
    res = binary_search(data, 13)
    print(res)
