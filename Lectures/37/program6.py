class StorageFull(BaseException):
    pass

try:
    x = int(input())
except StorageFull:
    print("StorageFul")
except ValueError:
    print("ValueError Exception")
