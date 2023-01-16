class Singleton:
    __instance=None

    """Here @staticmethod is decorator"""
    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance
    
    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance != None:
            raise Exception("You can't call it directly as it is singleton class. Call only using getInstance()")
        else:
            Singleton.__instance = self

s=Singleton();
print(s)

# s=Singleton();
# print(s)

s = Singleton.getInstance()
print(s)

s = Singleton.getInstance()
print(s)



