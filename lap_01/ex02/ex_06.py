# Nhập X và Y
input_str = input("Nhập X, Y: ")
dimensions = [int(x) for x in input_str.split(',')]
rowNum = dimensions[0]
colNum = dimensions[1]

# Tạo mảng hai chiều
multiList = [[0 for col in range(colNum)] for row in range(rowNum)]

# Điền giá trị cho mảng
for row in range(rowNum):
    for col in range(colNum):
        multiList[row][col] = row * col

# In kết quả
print(multiList)