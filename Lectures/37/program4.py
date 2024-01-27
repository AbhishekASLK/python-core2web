while True:
    try:
        age = int(input())
        break
    except ValueError:
       print("Oops!")
    else:
        print("No Exception Occured!")
    finally:
        print("finally")

print(age)

