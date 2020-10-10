#Ryan Nguyen
#Year Up Class 23 Python
#Working with files

from xlwt.compat import xrange
from xlwt import Workbook, Formula, easyxf
import os


print (os.getcwd())


if not os.path.exists('C:/Users/ryann/PycharmProjects/script4lab/Script9LabAssignment'):
    os.makedirs('C:/Users/ryann/PycharmProjects/script4lab/Script9LabAssignment')
else:
    pass


os.chdir('C:/Users/ryann/PycharmProjects/script4lab/Script9LabAssignment')

file = open('C:/Users/ryann/PycharmProjects/script4lab/Script9LabAssignment/file.txt', 'w')
text = file.write('This is my assignment for Lab 9. \nI know that it is easy to create text files in Python \nI just need to relax and follow the yellow brick road')
file.close()


print ("saved to file: " , text)

file = open('C:/Users/ryann/PycharmProjects/script4lab/Script9LabAssignment/file.txt', 'r')
print (file.read())

style1 = easyxf('pattern: pattern solid, fore_colour yellow;')
wb = Workbook()

sheet1 = wb.add_sheet('Sheet 1')

sheet1.write(0,0, 'Column 1')
sheet1.write(0,1, 'Column 2')
sheet1.write(0,2, 'Column 3')

for i in xrange(10):
    sheet1.write(i+1, 0, i + 1)
    sheet1.write(i+1, 1, (100 + 10 * i))
    sheet1.write(i + 1, 2, (1500 + 1500 * i))

sheet1.write(12, 0, Formula('SUM(A2:A11)'), style1)
sheet1.write(12, 1, Formula('SUM(B2:B11)'), style1)
sheet1.write(12, 2, Formula('SUM(C2:C11)'), style1)


wb.save("Lab9.xls")



