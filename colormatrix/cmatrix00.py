from colormatrix import *

for key, value in colors.items():
    print(f'{key:10} {value}')

# YOUR CODE HERE
atable = []
for row_index in range(N):
    arow = []
    for col_index in range(N):
        if row_index % 2 == 0:
            arow.append('black')
        else:
            arow.append('')
    atable.append(arow)
# DO NOT CHANGE THE FOLLOWING CODE
str_html = html_table(atable)
filename = __file__.rsplit('\\', 1)[-1].split('.')[0]
print(filename)
save_html(str_html, filename)
