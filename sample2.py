__author__ = 'rohit'

import os


file1 = open("/home/rohit/PycharmProjects/untitled/student.json", "r")
file2 = open("/home/rohit/PycharmProjects/untitled/student2.json", "w")
file2.write('[' + '\n')


for _ in xrange(2):
    file1.next()

line1 = file1.next()
print line1[len(line1)-3]

for line in file1:
    file2.write(line)
    if len(line) >=3 and line[len(line)-3] == ']':
        break

#for line in file1:
#    file2.write(line)

#file2.write('\n' + ']')
file1.close()
file2.close()
os.system("mongoimport -d mydb -c final /home/rohit/PycharmProjects/untitled/student2.json --jsonArray")
print 'json import sucessfully'


