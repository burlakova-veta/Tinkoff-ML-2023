import os
import sys

dir1, dir2, f_name = sys.argv[1:]
files = os.listdir(dir1)
res = ''
for i in range(len(files)):
    res += f'{dir1}/{files[i]} {dir2}/{files[i]}\n'
f = open(f_name, 'w')
f.write(res)
f.close()