def nextMove(n,r,c,grid):
    obj1 = list(enumerate(grid))
    obj2 = []
    for x in obj1:
        obj2.append(list(enumerate(x[1]))) 
    p_r,p_c = 0,0
    p_count_r = 0
    for i in obj2:
        p_count_c = 0
        for j in i:
            if (j[1] == "p"):
                p_r,p_c = p_count_r,p_count_c
            p_count_c += 1
        p_count_r += 1
    string = ""

    horizontal = p_c - c
    vertical = p_r - r

    if(vertical < 0):
        string = "UP"
    elif(vertical > 0):
        string = "DOWN"
    elif(horizontal < 0):
            string = "LEFT" 
    elif(horizontal > 0):
        string = "RIGHT"
            
    return f"{string}"

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))