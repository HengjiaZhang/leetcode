# 找到不小于(大于等于)这个数的第一个点
def find(target, lists):
    low = 0
    high = len(lists)
    while low < high:
        mid = (low + high) // 2
        # print((low, high, mid))
        if lists[mid] >= target:
            high = mid
        elif lists[mid] < target:
            low = mid + 1
    return low


# 找到大于这个数的第一个点
def find2(target, lists):
    return find(target+1, lists)


def find3(target, lists):
    low = 0
    high = len(lists)
    while low < high:
        mid = (low + high) // 2
        # print((low, high, mid))
        if lists[mid] <= target:
            low = mid+1
        else:
            high = mid
    return low


print(find(5, [1,2,2,4,5,5,5,5,5,5,5,6]))
print(find2(5, [1,2,2,4,5,5,5,5,5,5,5,6]))
print(find3(5, [1,2,2,4,5,5,5,5,5,5,5,6]))

