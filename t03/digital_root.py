def digital_root(data: int) -> int:
    if not isinstance(data, int):
        raise TypeError('Variable must be integer')
    if data < 0:
        raise ValueError('Number must be non-negative')

    number = data
    res = len(str(number))

    while (res > 1):
        tmp = 0

        for i in str(number):
            tmp += int(i)
        number = tmp
        res = len(str(number))
    return number
