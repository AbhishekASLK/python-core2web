class CustomError(BaseException):
    def __init__(self):
        print("CustomError constructor")
        self.message = "Custom SMS"
        super().__init__(self.message)

    def __str__(self):
        print("str method")

try:
    x = int(input())
    if(x>0):
        print(x)
    else:
        raise CustomError()
except CustomError:
    print("Exception occured: ",CustomError())

        
