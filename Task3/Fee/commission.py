def commission(balance, sum):
    if sum < 30:
        return balance - 30
    elif sum > 40000:
        return balance - 600
    else:
        return balance * 0.985
