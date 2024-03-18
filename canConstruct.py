def CanConstruct(target, wordBank, mem= None):
    # if mem is None: mem = {}
    # if target in mem: return True
    # target = target.lower()
    if target == "": return True
    for word in wordBank:
        if target.startswith(word):
            if CanConstruct(target[len(word):], wordBank):
                # mem[target] = True
                
                return True
    # mem[target] = False
    return False
def CanConstructDP(target, wordBank, mem= None):
    if mem is None: mem = {}
    if target in mem: return mem[target]
    # target = target.lower()
    if target == "": return True
    for word in wordBank:
        if target.startswith(word):
            if CanConstructDP(target[len(word):], wordBank, mem):
                mem[target] = True
                return True
    mem[target] = False
    return False



#test cases
def test_CanConstruct():
    assert (output := CanConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) == True, f"Test case 1 failed: {output}"
    assert (output := CanConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) == False, f"Test case 2 failed: {output}"
    assert (output := CanConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) == True, f"Test case 3 failed: {output}"
    # assert (output := CanConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) == False, f"Test case 4 failed: {output}"
def test_CanConstructDP():
    assert (output := CanConstructDP("abcdef", ["ab", "abc", "cd", "def", "abcd"])) == True, f"Test case 1 failed: {output}"
    assert (output := CanConstructDP("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) == False, f"Test case 2 failed: {output}"
    assert (output := CanConstructDP("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) == True, f"Test case 3 failed: {output}"
    assert (output := CanConstructDP("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) == False, f"Test case 4 failed: {output}"

# test_CanConstructDP()
# print(CanConstructDP("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))