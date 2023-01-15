import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
file = open(dir_path+'/Matrix.txt', 'r', encoding='utf-8')
fileArray = open(dir_path+'/array.txt', 'w+')

row = file.readlines()
last = len(row)
for i, a in enumerate(row):
    if i == 0:
        fileArray.write('[[' + ','.join(str(int(i)) for i in a.replace('\n', '').split(' ')) + '],')
    elif i == last-1:
        fileArray.write('[' + ','.join(str(int(i)) for i in a.replace('\n', '').split(' ')) + ']]')
    else:
        fileArray.write('[' + ','.join(str(int(i)) for i in a.replace('\n', '').split(' ')) + '],')
file.close()
fileArray.close()