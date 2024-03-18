def CountConstruct(target, wordBank, mem= None):

    if target == "": return 1
    count = 0
    for word in wordBank:
        if target.startswith(word):
            count += CountConstruct(target[len(word):], wordBank)            
    return count


def CountConstructDP(target, wordBank, mem= None):
    if mem is None: mem = {}
    if target in mem: return mem[target]
    if target == "": return 1
    count = 0
    for word in wordBank:
        if target.startswith(word):
            count += CountConstructDP(target[len(word):], wordBank, mem) 
    mem[target] = count           
    return count

#test cases
def test_CountConstruct():
    assert (output := CountConstructDP("purple", ["purp", "p", "ur", "le", "purpl"])) == 2, f"Test case 1 failed: {output}"
    assert (output := CountConstructDP("abcdef", ["ab", "abc", "cd", "def", "abcd"])) == 1, f"Test case 2 failed: {output}"
    assert (output := CountConstructDP("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) == 0, f"Test case 3 failed: {output}"
    assert (output := CountConstructDP("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) == 4, f"Test case 4 failed: {output}"
    assert (output := CountConstructDP("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) == 0, f"Test case 5 failed: {output}"

test_CountConstruct()