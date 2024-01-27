try:
    x = int(input())
except object:
    print("object")
except BaseException:
    print("BaseException")
except Exception:
    print("Exception")
except ValueError:
    print("ValueError Exception")
else:
    print("exception not occured")
