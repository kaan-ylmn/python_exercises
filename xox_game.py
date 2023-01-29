class Check_game():
    def __init__(self,liste1):
        self.liste1 = liste1
    
    def check_horizantal(self):
        number1 = 0 
        for _ in range(3):
            number2 = 0
            x_count = 0
            o_count = 0
            for _ in range(3):
                if self.liste1[number1][number2][1] == "X":
                    x_count += 1
                elif self.liste1[number1][number2][1] == "O":
                    o_count += 1
                number2 += 1
            if x_count == 3 or o_count == 3:
                return True
            number1 += 1

    def check_vertical(self):
        number1 = 0 
        for _ in range(3):
            number2 = 0
            x_count = 0
            o_count = 0
            for _ in range(3):
                if self.liste1[number2][number1][1] == "X":
                    x_count += 1
                elif self.liste1[number2][number1][1] == "O":
                    o_count += 1
                number2 += 1
            if x_count == 3 or o_count == 3:
                return True
            number1 += 1

    def check_cross(self):
        for _ in range(3):
            number1 = 0
            number2 = 2 
            x_count = 0
            o_count = 0
            for _ in range(3):
                if (self.liste1[number1][number1][1] == "X") or (self.liste1[number1][number2][1] == "O"):
                    x_count += 1
                elif self.liste1[number1][number1][1] == "O":
                    o_count += 1
                number1 += 1
                number2 -= 1
            if x_count == 3 or o_count == 3:
                return True

liste1 = []
for i in range(0,3):
    liste2 = []
    for j in range(0,3):
        liste2.append(".")
    liste2 = list(enumerate(liste2))    
    liste1.append(liste2)

aaa = 2
while True:
    while True:
        y_axis = int(input("y axis: "))
        x_axis = int(input("x axis: "))
        if not((0 <= x_axis < 3) and (0 <= y_axis < 3)):
            raise Exception("Please enter a valid number for y and x axis between 0 and 3")
        if not(liste1[y_axis][x_axis][1] == "X") or (liste1[y_axis][x_axis][1] == "O"):
            break

    character = "O"
    if aaa % 2 == 0:
        character = "X"
    aaa += 1

    point = liste1[y_axis]
    for x_value in point:
        x_value = list(x_value)
        if x_axis == x_value[0]:
            x_value[1] = character
            x_value = tuple(x_value)
            point[x_axis] = x_value
            
    for i in liste1:
        sum = ""
        for j in i:
            sum += j[1]
        print(sum)

    check_game = Check_game(liste1)
    if (check_game.check_horizantal() == True)  or (check_game.check_vertical() == True) or (check_game.check_cross() == True):
        break
