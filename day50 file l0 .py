# reading a file

f=open('myfile.txt','r')

text=f.read()
print(text)
f.close()


# writing a file

f=open('myfile.txt','w')
f.write('hello, rahul')
f.close()