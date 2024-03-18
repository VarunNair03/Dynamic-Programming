def HowSumDP(target, numbers, memo = None):
    if memo is None: memo = {}
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None
    sol = None
    for number in numbers:  
        remainder = target-number
        result = HowSumDP(remainder, numbers,memo)
        if result is not None: 
            if sol is None or len([*result, number]) < len(sol):
                sol = [*result, number]
    memo[target] = sol
    return memo[target]


def BestSumTab(target, numbers):
    tab = [None]*(target+1)
    tab[0] = []
    for i in range(target+1):
        if tab[i] is not None:
            for num in numbers:
                val = i + num
                if val <= target:
                    if tab[val] is None:
                        tab[val] = [*tab[i], num]
                    else:
                        tab[val] = [*tab[i], num] if len([*tab[i], num]) < len(tab[val]) else tab[val]
            

    return tab[target]
print(BestSumTab(7,[5,4,3,7]))