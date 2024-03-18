def HowSumDP(target, numbers, memo = None):
    if memo is None: memo = {}
    # print(target)
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None

    for number in numbers:
        
        remainder = target-number
        result = HowSumDP(remainder, numbers,memo)
        if result is not None: 
            memo[target] = [*result, number]
            return memo[target]   
    memo[target] = None
    return None 


def HowSumTab(target, numbers):
    tab = [None]*(target+1)
    tab[0] = []
    for i in range(target+1):
        if tab[i] is not None:
            for number in numbers:
                if  i + number <= target:
                    val = i+number
                    tab[val] = [*tab[i], number]

    return tab[target]
                    
                

#generate test cases
def test():
    assert (output := HowSumDP(7, [2, 3])) == [3, 2, 2], f"Test case 1 failed: {output}"
    assert (output := HowSumDP(7, [5, 3, 4, 7])) == [4, 3], f"Test case 2 failed: {output}"
    assert (output := HowSumDP(7, [2, 4])) == None, f"Test case 3 failed: {output}"
    assert (output := HowSumDP(8, [2, 3, 5])) == [3, 5] or [2,2,2,2], f"Test case 4 failed: {output}"
    assert (output := HowSumDP(300, [7, 14])) == None, f"Test case 5 failed: {output}"
    print("All test cases passed!")

# test()
# print(CanSumDP(8, [2, 3, 5]))
# print(HowSumDP(8, [2, 3, 5]))
print(HowSumTab(7,[5,4,3]))