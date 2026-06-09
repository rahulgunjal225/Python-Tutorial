
# CODE CHA FLOW THAMBLA NAHI PAHIJE MHANUN USED HOTO

a = int(input("PLEASE TELL YOUR 1ST NUMBER := "))
b = int(input("PLEASE TELL YOUR 2ND NUMBER := "))

try:                   # Wrap the risky code
    print(a/b)

except Exception as err:      # Handle the exception
    print(f"SORRY AN ERROR OCCURED AS {err}")

else:                      # Runs only if no exception occurred
    print("NO ERROR OCCURED" )

finally:                     # Always runs — good for cleanup
    print("IF THERE ARE ERROR OR THERE ARE NO ERROR I WILL RUN ALWAYS  ")

name = (input("TELL YOUR NAME :=  "))
print(f"HELLO YOUR NAME IS {name}")


# RAISE  [Manually throw your own exception]

age = int(input("TELL YOUR AGE :- "))

if age<18:
    raise TypeError("your are not eligible")

print("you are eligible")  