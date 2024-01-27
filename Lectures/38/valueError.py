try:
    x = int(input()
except SyntaxError:
    print('exception handled')
finally:
    print('finally')

'''
1. try akela nahi likha ja sakta,wah bas except ya phir finally chahta hai. 
2. agar maine finally likha try ke saath, to wah exception aane se pahle hi execute hoga, agar koi
   handling code na likha ho tab.

try:
    x = int(input())
finally:
    print('finally')

3. agar except likha hai to wah pahle except ko run karega and then last main finally ko
try:
    x = int(input())
except:
    print('exception handled')
finally:
    print('finally')

4. You can't handle SyntaxError Exception because it occured at the time of parsing
try:
    x = int(input()
except SyntaxError:
    print('exception handled')
finally:
    print('finally')
'''
