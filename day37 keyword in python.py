try:
    l=[1,4,6,8]
    i=int(input('enter the index: '))
    print(l[i])
except:
    print('some error occured')


finally:
    print('i am always executed')