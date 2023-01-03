import array as arr

def target_sum(data: arr.array, target: int) -> int:
    if not isinstance(data, arr.array):
        raise TypeError('Array must be NumPy ndarray type')
    if not isinstance(target, int):
        raise TypeError('Target must be integer')

    arr1 = data
    counter = 0

    for i in range(0, len(arr1)):
        for j in range(i+1, len(arr1)):
            if arr1[i] + arr1[j] == target:
                counter += 1
    return counter

res = target_sum(arr.array('i', [1, 3, 6, 2, 2, 0, 4, 5]), 5)
print(res)