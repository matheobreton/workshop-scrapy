def calculate(items):
    somme = 0
    ret = 0
    if len(items) < 2:
        return False
    for i in items:
        if (type(i) == str):
            try:
                somme += int(i)
            except:
                continue
            else:
                ret += 1
    if (ret < 2):
        return False
    else:
        return somme

print(calculate(['1', 3, '1', 2, 'dzee']))