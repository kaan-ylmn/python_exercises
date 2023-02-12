def save_princess(m,grid):
    directions = []
    for i in range(m):
        if "p" in grid[i]:
            liste = list(enumerate(grid[i]))
            middle_number = m // 2
            if i < middle_number:
                for x in range(middle_number):
                    if i == x:
                        for y in range(middle_number-i): 
                            directions.append("UP")
            if i > middle_number :
                for x in range(middle_number,m):
                    if i == x:
                        for y in range(i-middle_number): 
                            directions.append("DOWN")
    count = 0
    for j in liste:
        if "p" in j:
            x = count - middle_number
            if x < 0:
                for _ in range(-x):
                    directions.append("LEFT")
            if x > 0:
                for _ in range(x):
                    directions.append("RIGHT")
        count += 1
    print(directions)
    
m = int(input())
grid = []
for a in range(m):
    grid.append(input().strip())
save_princess(m,grid)
