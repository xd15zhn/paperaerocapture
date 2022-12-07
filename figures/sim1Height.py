import matplotlib.pyplot as plt
import numpy as np
import csv
import os
import sys

rows = []
with open('log.csv', 'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)
x = np.array(rows, dtype=np.float32)
x = x[:60]
t=np.linspace(0, 600, 60)
plt.plot(t, x)
# plt.show()

filename = os.path.basename(sys.argv[0])
filename = filename[:-3] + '.pdf'
print(filename)
plt.savefig(filename)
command = 'pdfcrop --margins "0 0 0 0" ' + filename + ' ' + filename
os.system(command)
