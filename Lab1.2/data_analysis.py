from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook ('data_analysis_lab.xlsx')
sheet = wb['Data']

A = sheet['A'][1:]
C = sheet['C'][1:]
D = sheet['D'][1:]

def getvalue(x): return x.value

A1 = list (map(getvalue, A))
C1 = list (map(getvalue, C))
D1 = list (map(getvalue, D))

print (list (A1))
print (list (C1))
print (list (D1))

pyplot.plot (A1, C1, label="Относит. температура")
pyplot.plot (A1, D1, label="Активность")

pyplot.show()