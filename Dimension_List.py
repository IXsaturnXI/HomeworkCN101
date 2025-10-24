#6810742681 เศรษฐการ มณีสวัสดิ์
#2 dimensions list
rows = int(input("Enter number of rows: "))
dim_list = []
#Left Pyramid
for i in range(1, rows + 1):
    row = ['*'] * i 
    dim_list.append(row)

for row in dim_list:
    print(*row, sep='')
dim_list.clear()
#Standard Pyramid
for i in range(1, rows + 1):
    num_spaces = rows - i
    spaces = [' '] * num_spaces
    
    num_stars = 2 * i - 1
    stars = ['*'] * num_stars
    
    row = spaces + stars
    dim_list.append(row)

for row in dim_list:
    print(*row, sep='')
dim_list.clear()
#Right Pyramid
for i in range(1, rows + 1):
    num_spaces = rows - i
    spaces = [' '] * num_spaces
    
    num_stars = i
    stars = ['*'] * num_stars
    
    row = spaces + stars
    dim_list.append(row)

for row in dim_list:
    print(*row, sep='')
dim_list.clear()


 
