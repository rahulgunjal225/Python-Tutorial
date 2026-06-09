
#  : Write a program to find out whether a given post is talking about “rahul” or not.


post = input("enetr the post : ")

if("rahul".lower in post.lower):
    print("this post is talking about rahul")

else:
    print('this is not talking about rahul')