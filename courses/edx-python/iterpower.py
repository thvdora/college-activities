def iterPower(base, exp):
    result = 1
    for i in range(exp):
        result = base * result
    return result
