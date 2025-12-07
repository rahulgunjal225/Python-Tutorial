# the seek and tell functioned are to used to work with the file objects,and their position within a file 


with open('myfile.txt','r')as f:
    print(type(f))

f.seek(10)
data=f.read(5)
print(data)