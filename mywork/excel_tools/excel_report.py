import xlsxwriter

workbook = xlsxwriter.Workbook('chart_line.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': 1})

# Add the worksheet data that the charts will refer to.
headings = ['Quarter', 'Excluding TM', 'Group']
data = [
    ['17Q1', '17Q2', '17Q3', '17Q4', '18Q1', '18Q2', '18Q3', '18Q4'],
    [1.92, 1.91, 1.91, 1.94, 2.0, 2.05, 2.08, 2.10],
    [1.74, 1.74, 1.73, 1.78, 1.83, 1.85, 1.86, 1.87],
    [1831, 1888, 1975, 2097, 2128, 2224, 2273, 2330]
]

worksheet.write_row('A1', headings, bold)
worksheet.write_column('A2', data[0])
worksheet.write_column('B2', data[1])
worksheet.write_column('C2', data[2])

# Create a new chart object. In this case an embedded chart.
chart1 = workbook.add_chart({'type': 'line'})

# Configure the first series.
chart1.add_series({
    'name':       '=Sheet1!$B$1',
    'categories': '=Sheet1!$A$2:$A$9',
    'values':     '=Sheet1!$B$2:$B$9',
})

# Configure second series. Note use of alternative syntax to define ranges.
chart1.add_series({
    'name':       ['Sheet1', 0, 2],
    'categories': ['Sheet1', 1, 0, 8, 0],
    'values':     ['Sheet1', 1, 2, 8, 2],
})

# Add a chart title and some axis labels.
chart1.set_title ({'name': ''})
chart1.set_x_axis({'name': 'Quarter'})
chart1.set_y_axis({'name': 'Net Interest Margin'})

# Set an Excel chart style. Colors with white outline and shadow.
chart1.set_style(2)

# Insert the chart into the worksheet (with an offset).
worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})


workbook.close()