def inputData():
    i = 0
    data = [] # data will contain 2 dimensional list, this is the return value
    while i < 9:
        res = input(f'Input data on row - {i + 1} : ')
        if not res.isdigit() or len(res) != 9: # possible error catch
            print('Input must be number and have 9 digit length')
        else:
            row = [] # row will contain the res input, but in integer type data
            for char in res:
                row.append(int(char))
            data.append(row)
            i += 1
    return data

def displayData(data):
    print('\nThis is your input data :')
    for i in range(9):
        for j in range(9):
            print(f' {data[i][j]}', end='')
        print('\n')

def checkingSudoku(data):
    data1 = data # set of horizontal data
    data2 = convertColumn(data) # set of vertical data
    data3 = convert3x3(data) # set of 3x3 data
    # x,y,z will return boolean value. if all true, then its sudoku.
    x = isSudoku(data1)
    y = isSudoku(data2)
    z = isSudoku(data3)
    return 'YES' if x and y and z else 'NO'

def isSudoku(data):
    counter = 1
    temp = []
    for i in range(9):
        [temp.append(x) for x in range(1, 10)]
        for j in range(9):
            if data[i][j] not in temp:
                return False
            else:
                temp.remove(data[i][j])
        temp.clear()
        counter += 1
    return True

def convertColumn(data):
    col = [] # this list will contain the set of column
    res = [] # return value, transposed list
    for i in range(9):
        for j in range(9):
            col.append(data[j][i])
        res.append(col)
    return res

def convertBlock(data, row, position):
    block = []
    counter_x = row * 3 # to limit the horizontal counter
    counter_y = position * 3 # to limit the vertical counter
    a = counter_x
    while a < counter_x + 3:
        b = counter_y
        while b < counter_y + 3:
            block.append(data[a][b])
            b += 1
        a += 1
    return block

def convert3x3(data):
    res = [] # this list will contain the converted data, 9 set of 3x3 blocks
    # data will be converted from left to right, then top to down
    for i in range(3): # left to right
        for j in range(3): # top to down
            block = convertBlock(data, i, j)
            res.append(block)
    return res

def main():
    data = inputData()
    displayData(data)
    print('Is this valid sudoku?', checkingSudoku(data))

if __name__ == "__main__":
    main()