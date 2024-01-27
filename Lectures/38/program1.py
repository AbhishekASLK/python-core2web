class CustomError(Exception):
    def __init__(self):
        print("CustomError Constructor")
        self.message = "Custom SMS"
        super().__init__(self.message)

try:
    x = int(input())
    if(x>0):
        print(y)
    else:
        raise CustomError
except CustomError as ce:
    print('Exception occured: ',ce)
