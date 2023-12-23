def decor1(func):
        def wrap():
               print("************")
               func()
               print("************")
        return wrap
def decor2(func):
        def wrap():
               print("@@@@@@@@@@@@")
               func()
               print("@@@@@@@@@@@@")
        return wrap
     
@decor2
        
@decor1
def sayhellogfg():
         print("Hello")
def saygfg():
         print("GeekforGeeks")
         
sayhellogfg()
saygfg()
