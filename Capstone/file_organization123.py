'''file = open("Dummy.txt")
print(file.read())
print(file)
print(file.name)
file.close()

with open('Dummy.txt','r')as file:  #context manager
    print(file.readline(), end =' ')
    print(file.readline(), end=' ')
    print(file.tell())

with open('Dummy.txt','r')as file:
    for line in file:
        print(line, end=' ')

with open('Dummy.txt','r')as file:
    file_content = file.read(3)
    print(file_content)

    file_content=file.readline()
    print(file_content,end='')
    print(file.tell())

file=open('Dummy.txt','r')
lines = ["Line 100","Line101"]
file.close()

sampleFile = open("Dummy.txt",'a')
sampleFile.write("This should append to a file")
sampleFile.close()

sampleFile = open("Dummy.txt",'w')
sampleFile.write("This should append to a file")
sampleFile.close()

file = open("Dummy.txt",'r+')
print(file.readable())
print(file.writable())
print(file.read())


file.seek(4)
print(file.tell())
print(file.readline())

file = open("Dummy.txt",'r')
print(file.readlines())

with open('Dummy.txt','r')as file, open('dummy1.txt','a') as file2:
    for l in file:
        file2.write(l)

file = open("Dummy.txt",'a')
file.truncate(10)
file.close()

for i in range(65,97):
     val=chr(i)
     name=str(val)+'.txt'
     with open(name,'x') as file1:
          file1.write(val)

file.flush()
print("+++++++++++")
print(file.read())
'''


file = open("Dummy.txt",'a')
file.truncate(10)
file.close()

