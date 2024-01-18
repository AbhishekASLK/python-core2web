

class Demo():
    @abstractmethod 
    def fun(self):
        print('in abstract fun')

obj = Demo()
obj.fun()
