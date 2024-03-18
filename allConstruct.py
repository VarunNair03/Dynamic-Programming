from time import time
def AllConstruct(target, wordBank, mem= None):

    if target == "": return [[]]
    res = []
    for word in wordBank:
        if target.startswith(word):
            counts = AllConstruct(target[len(word):], wordBank) 
            targetway =  [[word, *count] for count in counts]
            res.extend(targetway)
    return res

def AllConstructDP(target, wordBank, mem= None):
    if mem is None: mem = {}
    if target in mem: return mem[target]
    if target == "": return [[]]
    res = []
    for word in wordBank:
        if target.startswith(word):
            counts = AllConstructDP(target[len(word):], wordBank, mem) 
            targetway =  [[word, *count] for count in counts]
            res.extend(targetway)
    mem[target] = res
    return res



tic = time()
AllConstruct("aaaaaaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaaa", "aaa", "aaaaa"])
tock = time()
print("Time take is: ", tock-tic)

tic = time()
print(len(AllConstructDP("aaaaaaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaaa", "aaa", "aaaaa"])))
tock = time()
print("Time take is: ", tock-tic)