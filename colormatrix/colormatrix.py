# DO NOT CHANGE COLORS
colors = {
    'black'    : '#363636',
    'indianred': '#dd7e6b',
    'red'      : '#ea9999',
    'orange'   : '#f9cb9c',
    'yellow'   : '#ffe599',
    'green'    : '#b6d7a8',
    'cyan'     : '#a2c4c9',
    'royalblue': '#a4c2f4',
    'blue'     : '#9fc5e8',
    'purple'   : '#b4a7d6',
    'magenta'  : '#d5a6bd',
    'gray'     : '#e0e0e0',
    'white'    : '#ffffff',
}

# DO NOT CHANGE THIS FUNCTION
def html_table(atable):
    str_html = ''
    str_html += '<div style="margin-top: 20px; display: flex; justify-content: center;">'
    str_html += '<table style="border: 1px solid;">'
    atable.insert(0, ['gray' for _ in range(len(atable))])
    for ri, row in enumerate(atable):
        str_html += '<tr style="border: 1px solid;">'
        row = ['gray'] + row
        for ci, col in enumerate(row):
            if col == '':
                col = 'white'
            color = colors[col]
            str_html += f'<td style="background: {color}; width:20px; height: 20px; border: 1px solid; text-align: center;">'
            if ri == 0 and ci > 0:
                str_html += str(ci-1)
            elif ci == 0 and ri > 0:
                str_html += str(ri-1)
            str_html += '</td>'
        str_html += '</tr>'
    str_html += '</table>'
    str_html += '</div>'
    return str_html

# DO NOT CHANGE THIS FUNCTION
def save_html(str_html, filename):
    file = open(f'{filename}.html', 'w')
    file.write(str_html)
    file.close()

# NxN
N = 12