def first_non_repeating_letter(data: str) -> str:
    if not isinstance(data, str):
        raise TypeError('Variable must be a string')
    tmp_data = data.lower()
    for i in range(len(tmp_data)):
        counter = tmp_data.count(tmp_data[i])
        if counter == 1:
            return data[i]