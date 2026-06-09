# USE METHOD [DOES NOT USED ]

class hello:
    __a = 12

    @classmethod
    def info(cls):
        print(cls.__a)

obj = hello()
obj.info()