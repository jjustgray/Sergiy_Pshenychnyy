def sort_list(s: str) -> str:
    if not isinstance(s, str):
        raise TypeError('Variable must be string')
    s = s.upper()
    friends = s.split(';')
    names = []
    res = ""

    for i in friends:
        names.append(i.split(':'))
    for i in range(len(names)):
        names[i].reverse()
    names.sort()

    for i in range(len(names)):
        res += "("
        res += names[i][0]
        res +=", "
        res += names[i][1]
        res += ")"
    return res


s = "Fred:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
print(sort_list(s))
