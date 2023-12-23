def decor1(func):
    def inner():
        text = func()
        return text.upper()  # Convert text to uppercase
    return inner

def decor2(func):
    def inner():
        text = func()
        return text + " Decorated"  # Add ' Decorated' to the text
    return inner

@decor2
@decor1
def text_modifier():
    return "hello"

print(text_modifier())

