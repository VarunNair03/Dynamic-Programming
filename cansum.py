import time
# def CanSum(target, numbers):
#     if target == 0: return True
#     if target <= 0: return False

#     for number in numbers:
#         if CanSum(target-number, numbers): return True
#     return False

def CanSumDP(target, numbers, memo = None):
    if memo is None: memo = {}
    # print(target)
    if target in memo: return memo[target]
    if target == 0: return True
    if target < 0: return False

    for number in numbers:
        remainder = target-number
        if CanSumDP(remainder, numbers, memo): 
            memo[target] = True
            return True
    memo[target] = False
    return False

#generate test cases for CanSum


def CanSumTab(target, numbers):
    i = 0
    tab = [False] * (target+1)
    tab[0] = True
    while i <= target:
        for number in numbers:
            if  tab[i] and i+number <= target:
                tab[i+number] = True
        i += 1
    return tab[target]


# def test_CanSum():
#     print(CanSumDP(7, [2,3],{}))
#     print(CanSumDP(7, [5,3,4,7], {}))
#     print(CanSumDP(7, [2,4], {}))
#     print(CanSumDP(8, [2,3,5], {}))
#     print(CanSumDP(300, [7,14], {}))

# # # test_CanSum()
# print(CanSumDP(7, [2,3]))
# print(CanSumDP(7, [5,3,4,7]))
# print(CanSumDP(7, [2,4]))
# print(CanSumDP(8, [2,3,5]))
# print(CanSumDP(300, [7,14]))
    


tick = time.time()
print(CanSumTab(300, [2,3,5]))
tock = time.time()   
print("Time taken is: ",tock-tick)

tick = time.time()
print(CanSumDP(300, [2,3,5]))
tock = time.time()   
print("Time taken is: ",tock-tick)

