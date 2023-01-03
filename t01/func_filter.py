def filter_list(data):
    if type(data) != list:
        raise TypeError('Variable must be a list')
    for i in data:
        if type(i) == int or type(i) == float:
            if i < 0:
                raise ValueError('Numbers must be non-negative')
    new_data = []

    for i in data:
        if type(i) == int or type(i) == float:
            new_data.append(i)
    return new_data
    
   