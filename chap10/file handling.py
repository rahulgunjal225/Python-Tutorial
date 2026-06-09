
# CRUD operation

# open("FILE.txt","x")           # NEW TXT FILE CREATE KARNYA SATHI FKT 

#file = open("RAHUL.txt","w")           # NEW TXT FILE CREATE KARNYA SATHI ANI LIHNYA SATHI

#data = input("WHAT YOU WANT TO WRITE IN YOUR FILE :- ")

#file.write(data)


#file = open("RAHUL.txt","r")        # ALREADY CREATE KELE FILE MADHI ASLELA CONTENT VACHNYA SATHI READ OPTION 

#print(file.read())

with open("FILE.txt","a") as fl:              # FILE MADHI KAHI PN LIHU SHAKTO CHANGES KARU SHKTO
    fl.write(" " + "I WANT TO SEE IF IF IS WROKING OR NOT")