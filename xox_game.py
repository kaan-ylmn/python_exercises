class Check_game():
    def __init__(self,list1):
        self.list1 = list1
    
    def check_horizantal(self):
        for number1 in range(3):
            x_count = 0
            o_count = 0
            for number2 in range(3):
                if self.list1[number1][number2][1] == "X":
                    x_count += 1
                elif self.list1[number1][number2][1] == "O":
                    o_count += 1
            if x_count == 3 or o_count == 3:
                return True

    def check_vertical(self):
        for number1 in range(3):
            x_count = 0
            o_count = 0
            for number2 in range(3):
                if self.list1[number2][number1][1] == "X":
                    x_count += 1
                elif self.list1[number2][number1][1] == "O":
                    o_count += 1
            if x_count == 3 or o_count == 3:
                return True

    def check_cross(self):
        number2 = 2 
        rx_count = 0
        lx_count = 0
        ro_count = 0 
        lo_count = 0
        for number1 in range(3):
            if self.list1[number1][number1][1] == "X":
                rx_count += 1
            if self.list1[number1][number2][1] == "X":
                lx_count += 1
            if self.list1[number1][number1][1] == "O":
                ro_count += 1
            if self.list1[number1][number2][1] == "O":
                lo_count += 1
            number2 -= 1 
        if (rx_count == 3) or (lx_count == 3) or (ro_count == 3) or (lo_count == 3):
            return True

list1 = []
for i in range(0,3):
    list2 = []
    for j in range(0,3):
        list2.append(".")
    list2 = list(enumerate(list2))    
    list1.append(list2)

count = 2
while True:
    while True:
        y_axis = int(input("y axis: "))
        x_axis = int(input("x axis: "))
        if not((0 <= x_axis < 3) and (0 <= y_axis < 3)):
            raise Exception("Please enter a valid number for y and x axis between 0 and 3")
        if not((list1[y_axis][x_axis][1] == "X") or (list1[y_axis][x_axis][1] == "O")):
            break

    character = "O"
    if count % 2 == 0:
        character = "X"
    count += 1

    point = list1[y_axis]
    for x_value in point:
        x_value = list(x_value)
        if x_axis == x_value[0]:
            x_value[1] = character
            x_value = tuple(x_value)
            point[x_axis] = x_value
            
    for i in list1:
        sum = ""
        for j in i:
            sum += j[1]
        print(sum)

    check_game = Check_game(list1)
    if (check_game.check_horizantal() == True)  or (check_game.check_vertical() == True) or (check_game.check_cross() == True):
        break
