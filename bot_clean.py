board = ["----d","-----","-----","-----","-----"]
dirty_column = 0
dirty_row = 0
row = 0
posr = 2
posc = 3
for x in board:
    if("d" in x):
        dirty_row = row
        column = 0
        for y in x:
            if("d" == y):
                dirty_column = column
                break
            column += 1
    row += 1

while((dirty_row != posr) or (dirty_column != posc)):
    if((dirty_column - posc) > 0):
        posc += 1
        print("RIGHT")
    elif((dirty_column - posc) < 0):
        posc -= 1
        print("LEFT")
    elif((dirty_row - posr) > 0):
        posr += 1
        print("DOWN")
    elif((dirty_row - posr) < 0):
        posr -= 1
        print("UP")


