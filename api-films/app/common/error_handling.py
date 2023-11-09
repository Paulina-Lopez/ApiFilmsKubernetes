class AppErrorBaseClass(Exception):
    print(Exception)

class ObjectNotFound(AppErrorBaseClass):
    print(AppErrorBaseClass)
