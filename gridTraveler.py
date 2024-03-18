import time
def GridTravelerDP(m,n,dict = {}):
    # m is rows and n is columns
    if m == 0 or n == 0:
        return 0
    if m == n == 1:
        return 1
    
    if ((str(m) + "," + str(n)) in dict):
        return dict[str(m) + "," + str(n)]
    elif ((str(n) + ","  + str(m)) in dict):
        return dict[(str(n) + ","  + str(m))]
    else: 
        dict[str(m) + "," + str(n)] = GridTravelerDP(m-1,n, dict) + GridTravelerDP(m,n-1, dict)
        return dict[str(m) + "," + str(n)]
    
# def GridTraveler(m,n):
#     # m is rows and n is columns
#     if m == 0 or n == 0:
#         return 0
#     if m == n == 1:
#         return 1
#     return GridTraveler(m-1,n) + GridTraveler(m,n-1)
# tick = time.time()
# print(GridTraveler(29,29))
# tock = time.time()
# print("without Dp the time is: ",tock-tick)


# tick = time.time()
# print(GridTravelerDP(18,18))
# tock = time.time()
# print("with Dp the time is: ",tock-tick)
# generate test cases for GridTraveler
# def test_GridTraveler():
#     print(GridTravelerDP(1,1))
#     print(GridTravelerDP(2,3))
#     print(GridTravelerDP(3,2))
#     print(GridTravelerDP(3,3))
#     print(GridTravelerDP(18,18))
#     print(GridTravelerDP(29,29))

def GridTravelerTab(m,n):
    grid = [[0 for i in range(n+1)] for y in range(m+1)]

    grid[1][1] = 1
    for i in range(1,m+1):
        for j in range(1,n+1):
            grid[i][j] += grid[i][j-1]
            grid[i][j] += grid[i-1][j]
    return grid[m][n]

tick = time.time()
print(GridTravelerTab(200,18))
tock = time.time()
print("Time taken is: ",tock-tick)
            
tick = time.time()
print(GridTravelerDP(200,18))
tock = time.time()
print("Time taken is: ",tock-tick)
# GridTravelerTab(4,3)

# test_GridTraveler()

