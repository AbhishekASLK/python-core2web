class LowBatteryException(Exception):
    def __init__(self):
        self.message = 'Please charge the phone!'
        super().__init__(self.message)


try:
    n = int(input("Enter the charge %: "))
    if(n<15):
        raise LowBatteryException()

except LowBatteryException as instance:
    print("Warning: ",instance)
