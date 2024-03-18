def GCD(a,b):
    if b > a:
        while b:   
                a,b = b,b % a
        return a
            

def CoPrime():
    for i in range(1,101):
        for j in range(1,101):
            if i != j and GCD(i,j) == 1:
                print(f"[{i},{j}]")
# CoPrime()

print(GCD(4,3),GCD(3,4))
    