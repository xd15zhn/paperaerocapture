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
t = x[:, 0]
x = x[:, 1:]
x[:, 1] *= 50
x[:, 2] *= 0.02
plt.plot(t, x)
plt.legend([r'h', r'$\sigma\times 50$', r'$v_z\times 0.02$'])
# plt.show()
print(x.shape)

filename = os.path.basename(sys.argv[0])
filename = filename[:-3] + '.pdf'
print(filename)
plt.savefig(filename)
command = 'pdfcrop --margins "0 0 0 0" ' + filename + ' ' + filename
os.system(command)
