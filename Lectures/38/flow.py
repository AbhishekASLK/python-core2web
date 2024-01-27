try:
    x = int(input())
except KeyError:
    print('KeyError')
except ValueError:
    print('ValueError')


'''
1. except: default waala last main hi likha jana chahiye otherwise you will get compile time error

try:
    x = int(input())
except:
    print('except')
except ValueError:
    print('ValueError')

SyntaxError: default 'except:' must be last

2. Duplicate except bhi lihe ja shakte hai

try:
    x = int(input())
except ValueError:
    print('except')
except ValueError:
    print('ValueError')

3. Jo pahle likha hoga aur wah catch karne main saksham hoga to wahi block execute hoga, 
rather than going to find exact match

try:
    x = int(input())
except BaseException:
    print('except')
except ValueError:
    print('ValueError')

4. 
try:
    x = int(input())
except KeyError:
    print('KeyError')
except ValueError:
    print('ValueError')
'''
