def beautyparlour(bridetomakeup):
    def inner(name):
        print("I'm doing facial")
        bridetomakeup(name)
    return inner

def bride(name):
    print("I'm wearing saari!")

bride('Shashi')
